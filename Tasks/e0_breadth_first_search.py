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
    lst_v = []

    queue.append(start_node)
    lst_v.append(start_node)

    while queue:
        nd = queue.pop(0)
        neib = nx.neighbors(g, nd)
        for n in neib:
            if n not in lst_v:
                queue.append(n)
                lst_v.append(n)
    
    #print(g, start_node)
    return lst_v


def bfs_(g: nx.Graph, start_node: Hashable) -> List[Hashable]: # доделать
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
                queue.append(nb_nodes)
    return nodes

