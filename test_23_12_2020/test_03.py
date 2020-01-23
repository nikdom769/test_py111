"""
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов
"""

from typing import Hashable, List
import networkx as nx



def cnt_bind(func):
    """Поиск компоненты связанности"""
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
def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
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
    print(nodes) # (g, start_node)
    return nodes #list(g.nodes)


if __name__ == "__main__":
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([('A', 'B'),
                          ('B', 'C'),
                          ('C', 'D'),
                          ('F', 'G'),
                          ])
    dfs(graph, 'A')