"""
A                         C
############################
#						   # #
#						   #	#
#						   #		# E
#						   #		#
#						   #	#
#						   # #
############################
B						   D

"""
# adj_list = {
# 	"A":['B','C'],
# 	"B":['A','D'],
# 	"C":['A','D','E'],
# 	"D":['B','C','E'],
# 	"E":['C','D'],
# }

class Graph:
	"""docstring for Graph"""
	def __init__(self, Nodes,is_directred=False):
		self.nodes = Nodes
		self.adj_list = {}
		self.is_directred= is_directred
		for node in self.nodes:
			self.adj_list[node] = []

	def add_edge(self,u,v):
		self.adj_list[u].append(v)
		if not self.is_directred:
			self.adj_list[v].append(u)

	def degree(self,node):
		return len(node,self.adj_list[node])
	
	def print_adj_list(self):
		for node in self.nodes:
			print("{} -> {}".format(node,self.adj_list[node]))

all_edges = [
("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")
]
nodes = ['A','B','C','D','E']
graph = Graph(nodes,is_directred=True)
# graph = Graph(nodes)

for u,v in all_edges:
	graph.add_edge(u,v)

graph.print_adj_list()