from typing import Hashable, List
import networkx as nx


def search_node(func):
	"""
	Поиск пути до узла
	"""
	dest = "E"
	def wrp_dfs(*args):
		res = func(*args)
		for ind, elem in enumerate(res):
			if elem == dest and ind != 0:
				return res[0:ind+1]
	return wrp_dfs


def cnt_bind(func):
	"""
	Поиск компоненты связанности
	"""
	def wrp_dfs(*args):
		cnt = 1
		all_nodes = nx.nodes(args[0])
		res = func(*args)
		all_nodes = list(set(all_nodes) - set(res))
		while all_nodes:
			cnt += 1
			args = [args[0], all_nodes[0]]
			res = func(*args)
			all_nodes = list(set(all_nodes) - set(res))
		print(f"Связанность графа {cnt}")
	return wrp_dfs


@cnt_bind
#@search_node
def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""

	stack = []
	nodes = []
	stack.append(start_node)

	while stack:
		nd = stack.pop()
		if nd not in nodes:
			nodes.append(nd)
			nb_nodes = nx.neighbors(g, nd)
			if nb_nodes:
				stack.extend(nb_nodes)

	print(nodes)# (g, start_node)
	return nodes #list(g.nodes)


if __name__ == "__main__":
	graph = nx.Graph()
	graph.add_nodes_from("ABCDEFG")
	graph.add_edges_from([('A', 'B'),
						  ('A', 'C'),
						  ('B', 'D'),
						  #('B', 'E'),
						  ('C', 'F'),
						  ('E', 'G'),
						  ('E', 'H'),
						  ])

	dfs(graph, 'A')
