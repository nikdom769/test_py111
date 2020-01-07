from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, 'node3': 33, ...} with path costs, where nodes are nodes from g
    """
    
    queue = []
    queue.append(starting_node)
    
    path_coasts = {nm: float("inf") for nm in nx.nodes(g)}
    path_coasts[starting_node] = 0
    weight_edges = nx.get_edge_attributes(g, 'weight')

    while queue:
        nd = queue.pop(0)
        edge_nd = nx.edges(g, nd) # out edges
        if edge_nd:
            for eg in edge_nd:
                if path_coasts[nd] + weight_edges[eg] < path_coasts[eg[1]]:
                    queue.append(eg[1])
                    path_coasts[eg[1]] = path_coasts[nd] + weight_edges[eg]
    #print(path_coasts)
    return path_coasts
