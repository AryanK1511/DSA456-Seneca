class SetList:
	class Node:
		def __init__(self, data, set_list, next_node = None, prev_node = None):
			self.data = data
			self.set_list = set_list
			self.next_node = next_node
			self.prev_node = prev_node

		# Function returns data stored in node
		def get_data(self):
			return self.data

		# Function returns reference to next node in SetList
		def get_next(self):
			return self.next_node

		# Function returns reference to previous node in SetList
		def get_previous(self):
			return self.prev_node

		# Function returns reference to the SetList
		def get_set(self):
			return self.set_list

	def __init__(self):
		self.front = None
		self.back = None
	# This function returns a reference to the first node in the list
	def get_front(self):
		return self.front

	# This function returns a reference to the last node in the list
	def get_back(self):
		return self.back

	# This function adds the first value to the SetList object
	def make_set(self, data):
		new_node = self.Node(data, self)
		if self.front is None:
			self.front = new_node
			self.back = new_node
			return self.front
		else:
			return None

	# This function is passed a SetList and performs a union with the current object
	def union_set(self, set_list):
		if set_list:
			# Update the set_list attribute of each node in set_list
			current_node = set_list.get_front()
			while current_node:
				current_node.set_list = self
				current_node = current_node.get_next()

			# Merge the linked lists
			# Follows two different approached based on whether our merge list is empty or not
			if self.back is None and self.front is None:
				self.front = set_list.get_front()
			else:
				if set_list.get_front() is not None:
					self.back.next_node = set_list.get_front()
					set_list.get_front().prev_node = self.back
			self.back = set_list.get_back()

			# Set the set_list to be empty
			set_list.front = None
			set_list.back = None

		return len(self)

	# This function is passed a data value, the function returns a reference to the Node containing data
	def find_data(self, data):
		current_node = self.front
		while current_node:
			if current_node.get_data() == data:
				return current_node
			current_node = current_node.get_next()
		return None

	# This function returns a reference to the node that holds the representative of the SetList
	def representative_node(self):
		ref = self.front if (self.front is not None) else None
		return ref

	# This function returns the data of the representative node of the SetList.
	def representative(self):
		representative_node = self.representative_node()
		data = representative_node.get_data() if (representative_node is not None) else None
		return data

	# This function returns the number of items within the SetList.
	def __len__(self):
		count, currNode = 0, self.front
		while currNode is not None:
			count += 1
			currNode = currNode.get_next()
		return count