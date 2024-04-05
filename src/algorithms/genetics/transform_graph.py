import networkx as nx
import numpy as np

START_NODE = '0'

def change_graph(graph, orders):
    nodes = list(orders.keys())

    shortest_path = nx.shortest_path(graph)
    nodes = [START_NODE] + [str(node) for node in nodes]
    
    transformed_graph = nx.Graph()

    for src in nodes:
        for dst in nodes:
            if src == dst:
                continue
            path = shortest_path[src][dst]

            edge_data = dict(
                path=path,
                distance = len(path) - 1 ,
            )

            transformed_graph.add_edge(src, dst, **edge_data)

    nx.set_node_attributes(transformed_graph, {
        node: {"weight": orders.get(int(node), np.inf)}
        for node in nodes
    })

    max_distance = max(
        transformed_graph[u][v]['distance']
        for u, v in transformed_graph.edges
    )

    nx.set_edge_attributes(transformed_graph, {
        (u, v): {
            "distance_norm": transformed_graph[u][v]['distance'] / max_distance
        }
        for u, v in transformed_graph.edges
    })

    return transformed_graph