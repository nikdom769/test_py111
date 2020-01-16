from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	queue = []
	nodes = []

	queue.append(start_node)

	while queue:
		nd = queue.pop(0)
		if nd not in nodes:
			nodes.append(nd)
			nb_nodes = nx.neighbors(g, nd)
			if nb_nodes:
				queue.append(nd_nodes)

	print(nodes)#(g, start_node)
	return nodes #list(g.nodes)
