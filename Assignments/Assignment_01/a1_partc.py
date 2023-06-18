from a1_partb import SetList

class DisjointSet:
	def __init__(self):
		self.disjointSet = {}

	def make_set(self, element):
		if element in self.disjointSet:
			return False
		else:
			setList = SetList()
			self.disjointSet[element] = setList
			setList.make_set(element)
			return True
	def get_set_size(self,element):
		for key, value in self.disjointSet.items():
			if value.find_data(str(element)):
				return len(value)
		return 0

	def find_set(self, element):
		for set_list in self.disjointSet.values():
			found = set_list.find_data(str(element))
			if found is not None:
				return set_list.representative()
		return False

	def union_set(self, element1, element2):
		for value in self.disjointSet.values():
			if value.find_data(str(element1)) is not None:
				node1 = value.find_data(str(element1))
			if value.find_data(str(element2)) is not None:
				node2 = value.find_data(str(element2))
				key = value.representative()

		if node1.get_set() != node2.get_set():
			node1.get_set().union_set(node2.get_set())
			self.disjointSet.pop(key)
			return True

		return False

	def update_set_references(self, source_set, target_set):
		current_node = source_set.get_front()
		while current_node:
			current_node.set_list = target_set
			current_node = current_node.get_next()
			
	def get_num_sets(self):
		return len(self.disjointSet)
	def __len__(self):
		count = 0
		for element in self.disjointSet.values():
			count += len(element)
		return count
