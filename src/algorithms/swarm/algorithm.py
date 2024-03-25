import networkx as nx

from .ant import Ant, START_NODE


def ant_algorithm():
    # temp mocks
    graph = nx.Graph()
    ants = [
        Ant(graph, max_capacity=10, velocity_factor=1),
        Ant(graph, max_capacity=10, velocity_factor=1),
    ]
    iterations = 100

    for _ in range(iterations):
        pass


def algorithm_iteration(ant):
    
    for ant in ants:
        ant.reset()


def simulate(graph, ants):
    while True:
        for ant in ants:
            ant.tick()

        if stop_condition():
            break

    def stop_condition():
        weights_left = sum(
            graph.nodes[node]['weight']
            for node in graph.neighbors(START_NODE)
        )
        return weights_left <= 0 and all(
            ant.path[-1] == START_NODE
            for ant in ants
        )


# class AntAlgorithm:
#     def __init__(self, order, warehouse) -> None:
#         # self.order = order
#         # self.warehouse = warehouse
#         # print(self.order)
#         # print(self.warehouse)
