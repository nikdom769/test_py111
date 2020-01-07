from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order
    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    
    steck = []
    lst_v = []

    steck.append(start_node)
    #lst_v.append(start_node)

    while steck:
        nd = steck.pop()
        lst_v.append(nd)
        neib = nx.neighbors(g, nd)
        for n in neib:
            if n not in lst_v:
                steck.append(n)
    
    
    #print(lst_v)
    return lst_v #list(g.nodes)
