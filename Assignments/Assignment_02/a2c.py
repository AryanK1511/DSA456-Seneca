class LinearProbingTS:
	pass
	class Record:
		# Status: 'E' => Empty, 'X' => Deleted, 'O' => Occupied
		def __init__(self, key = None, value = None, status = 'E'): 
			self.key = key
			self.value = value
			self.status = status

	# The initializer for the table defaults the initial table capacity to 32
	def __init__(self, cap = 32):
		self.cap = cap
		self.hash_table = [self.Record(None, None, 'E') for _ in range(cap)]
		self.elements = 0

	# This function adds a new key-value pair into the table
	def insert(self, key, value):
		if self.elements < self.cap:
			hashed_index = hash(key) % self.cap
			if self.hash_table[hashed_index].status != 'O' or self.hash_table[hashed_index].status == 'X':
				self.hash_table[hashed_index].key = key
				self.hash_table[hashed_index].value = value
				self.hash_table[hashed_index].status = 'O'
				self.elements += 1
				if ((self.elements / self.cap) >= 0.7):
					self.resize()
				return True
			else:
				while self.hash_table[hashed_index].status == 'O':
					if self.hash_table[hashed_index].key == key:
						return False
					hashed_index = (hashed_index + 1) % self.cap
				self.hash_table[hashed_index].key = key
				self.hash_table[hashed_index].value = value
				self.hash_table[hashed_index].status = 'O'
				self.elements += 1
				if ((self.elements / self.cap) >= 0.7):
					self.resize()
				return True
		return False

	# This function modifies an existing key-value pair into the table
	def modify(self, key, value):
		hashed_index = hash(key) % self.cap
		orig_index = hashed_index
		if self.hash_table[hashed_index].status == 'O' and self.hash_table[hashed_index].key == key:
			self.hash_table[hashed_index].value = value
			return True
		else:
			while self.hash_table[hashed_index].status != 'E' and self.hash_table[hashed_index].status != 'X':
				hashed_index = (hashed_index + 1) % self.cap
				if hashed_index == orig_index:
					break
				if self.hash_table[hashed_index].key == key:
					self.hash_table[hashed_index].value = value
					return True
		return False

	# This function removes the key-value pair with the matching key
	def remove(self, key):
		hashed_index = hash(key) % self.cap
		curr_index = hashed_index
		if self.hash_table[curr_index].key == key and self.hash_table[curr_index].status != 'X':
				self.hash_table[curr_index].status = 'X'
				self.elements -= 1
				return True
		else:
			while self.hash_table[curr_index].status != 'E':
				curr_index = (curr_index + 1) % self.cap
				if hashed_index == curr_index:
					break
				if self.hash_table[curr_index].key == key and self.hash_table[curr_index].status != 'X':
					self.hash_table[curr_index].status = 'X'
					self.elements -= 1
					return True
		return False
	
	# This function returns the value of the record with the matching key
	def search(self, key):
		hashed_index = hash(key) % self.cap
		orig_index = hashed_index
		if self.hash_table[hashed_index].status != 'E' and self.hash_table[hashed_index].status != 'X' and self.hash_table[hashed_index].key == key:
			return self.hash_table[hashed_index].value
		else:
			while self.hash_table[hashed_index].status != 'E':
				hashed_index = (hashed_index + 1) % self.cap
				if hashed_index == orig_index:
					break
				if self.hash_table[hashed_index].status == 'O' and self.hash_table[hashed_index].key == key:
					return self.hash_table[hashed_index].value
		return None

	# This function returns the number of spots in the table
	def capacity(self):
		return self.cap

	# This function returns the number of Records stored in the table
	def __len__(self):
		return self.elements

	# This function grows the underlying array used to implement the hash table
	def resize(self):
		self.cap *= 2
		old_table = self.hash_table
		self.hash_table = [self.Record(None, None, 'E') for _ in range(self.cap)]
		self.elements = 0
		for record in old_table:
			if record.status == 'O':
				self.insert(record.key, record.value)

class LinearProbingNoTS:
	class Record:
		def __init__(self, key = None, value = None):
			self.key = key
			self.value = value

	def my_hash(self, key):
		return sum(key.encode())
	
	# The initializer for the table defaults the initial table capacity to 32
	def __init__(self, cap = 32):
		self.cap = cap
		self.hash_table = [None for _ in range(cap)]
		self.elements = 0

	# This function adds a new key-value pair into the table
	def insert(self, key, value):
		if self.elements < self.cap:
			hashed_index = self.my_hash(key) % self.cap
			if self.hash_table[hashed_index] is None:
				self.hash_table[hashed_index] = self.Record(key, value)
				self.elements += 1
				self.resize()
				return True
			else:
				while self.hash_table[hashed_index] is not None:
					if self.hash_table[hashed_index].key == key:
						return False
					hashed_index = (hashed_index + 1) % self.cap
				self.hash_table[hashed_index] = self.Record(key, value)
				self.elements += 1
				self.resize()
				return True
		return False
			
	# This function modifies an existing key-value pair into the table
	def modify(self, key, value):
		hashed_index = self.my_hash(key) % self.cap
		if self.hash_table[hashed_index] is not None and self.hash_table[hashed_index].key == key:
			self.hash_table[hashed_index].value = value
			return True
		else:
			while self.hash_table[hashed_index] is not None:
				hashed_index = (hashed_index + 1) % self.cap
				if self.hash_table[hashed_index] is not None and self.hash_table[hashed_index].key == key:
					self.hash_table[hashed_index].value = value
					return True
		return False

	# This function removes the key-value pair with the matching key
	def remove(self, key):
		hashed_index = self.my_hash(key) % self.cap
		curr_index = hashed_index
		while self.hash_table[curr_index] is not None:
			if self.hash_table[curr_index].key == key:
				self.hash_table[curr_index] = None
				empty_index = curr_index
				next_index = (empty_index + 1) % self.cap
				while self.hash_table[next_index] is not None:
					if (empty_index >= self.my_hash(self.hash_table[next_index].key) % self.cap) and (empty_index < next_index):
						self.hash_table[empty_index] = self.hash_table[next_index]
						self.hash_table[next_index] = None
						empty_index = next_index
					next_index = (next_index + 1) % self.cap
				self.elements -= 1
				return True		
			curr_index = (curr_index + 1) % self.cap
		return False
		
	# This function returns the value of the record with the matching key
	def search(self, key):
		hashed_index = self.my_hash(key) % self.cap
		if self.hash_table[hashed_index] is not None and self.hash_table[hashed_index].key == key:
			return self.hash_table[hashed_index].value
		else:
			while self.hash_table[hashed_index] is not None:
				hashed_index = (hashed_index + 1) % self.cap
				if self.hash_table[hashed_index] is not None and self.hash_table[hashed_index].key == key:
					return self.hash_table[hashed_index].value
		return None

	# This function returns the number of spots in the table
	def capacity(self):
		return self.cap

	# This function returns the number of Records stored in the table
	def __len__(self):
		return self.elements
	
	# This function grows the underlying array used to implement the hash table
	def resize(self):
		if ((self.elements / self.cap) >= 0.7):
			self.cap *= 2
			old_table = self.hash_table
			self.hash_table = [None for _ in range(self.cap)]
			self.elements = 0
			for record in old_table:
				if record is not None:
					self.insert(record.key, record.value)