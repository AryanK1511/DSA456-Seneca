class Graph:

	def __init__(self, number_of_verts):
		self.number_of_verts = number_of_verts
		self.adjacency_list = [[] for _ in range(number_of_verts)]

	def add_vertex(self):
		self.adjacency_list.append([])
		self.number_of_verts += 1

	def add_edge(self, from_idx, to_idx, weight=1):
		if 0 <= from_idx < self.number_of_verts and 0 <= to_idx < self.number_of_verts:
			for vertex_edges in self.adjacency_list[from_idx]:
				if vertex_edges[0] == to_idx:
					return False
			
			self.adjacency_list[from_idx].append((to_idx, weight))
			return True
		else:
			return False		

	def num_edges(self):
		count = 0
		for vertex_edges in self.adjacency_list:
			count += len(vertex_edges)
		return count

	def num_verts(self):
		return self.number_of_verts
	
	def has_edge(self, from_idx, to_idx):
		if 0 <= from_idx < self.number_of_verts and 0 <= to_idx < self.number_of_verts:
			for vertex_edges in self.adjacency_list[from_idx]:
				if vertex_edges[0] == to_idx:
					return True
		return False
	
	def edge_weight(self, from_idx, to_idx):
		if 0 <= from_idx < self.number_of_verts and 0 <= to_idx < self.number_of_verts:
			for vertex_edges in self.adjacency_list[from_idx]:
				if vertex_edges[0] == to_idx:
					return vertex_edges[1]
		return None
	
	def get_connected(self, v):
		if 0 <= v < self.number_of_verts:
			return self.adjacency_list[v]
		return []