import networkx as nx
import numpy as np

START_NODE = '0'

# def change_graph(graph):
#     shortest_paths = dict(nx.all_pairs_shortest_path(graph))
    
#     transformed_graph = nx.Graph()
    
#     for src in graph.nodes:
#         for dst in graph.nodes:
#             if src == dst:
#                 continue
            
#             if dst in shortest_paths[src]:
#                 shortest_path = shortest_paths[src][dst]
                
#                 distance = len(shortest_path) - 1
                
#                 transformed_graph.add_edge(src, dst, distance=distance) #bidirectional
#                 transformed_graph.add_edge(dst, src, distance=distance)
    
#     max_distance = max(nx.get_edge_attributes(transformed_graph, 'distance').values())
    
#     for _, _, data in transformed_graph.edges(data=True):
#         distance_norm = data['distance'] / max_distance
#         data['distance_norm'] = float("{:.2f}".format(distance_norm))
                
#     return transformed_graph

def change_graph(graph, orders):
    shortest_paths = nx.shortest_path(graph)

    nodes = list(orders.items.keys())
    nodes = [START_NODE] + [str(node) for node in nodes]
    graph = nx.Graph()

    for src in nodes:
        for dst in nodes:
            if src == dst:
                continue
            try:
                path = shortest_paths[src][dst]
            except KeyError:
                # Handle missing path gracefully, for example, setting a default path
                path = [src, dst]

            edge_data = dict(
                path=path,
                distance=len(path) - 1,
            )

            graph.add_edge(src, dst, **edge_data)

    # nx.set_node_attributes(graph, {
    #     node: {
    #         "weight": orders.get(int(node), np.inf),
    #         "weight_left": orders.get(int(node), np.inf),
    #     }
    #     for node in nodes
    # })

    max_distance = max(
        graph[u][v]['distance']
        for u, v in graph.edges
    )

    nx.set_edge_attributes(graph, {
        (u, v): {
            "distance_norm": graph[u][v]['distance'] / max_distance
        }
        for u, v in graph.edges
    })

    return graph

# graph = nx.read_adjlist('../../../generated_graphs/graph_4_4.adjlist')
# x = change_graph(graph)
# print(x)