import networkx as nx

class Warehouse:
    def __init__(self, txt_file, robots) -> None:
        self.graph = nx.read_adjlist(txt_file)
        self.robots = robots

    # generate warehouse graph with wages
        # G.add_node(1, weight=10)
        # G.add_node(2, weight=15)
        # G.add_node(3, weight=20)

        # G.add_edge(1, 2, weight=5)
        # G.add_edge(2, 3, weight=7)
        # G.add_edge(1, 3, weight=9)
