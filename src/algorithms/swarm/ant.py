import math
import random


START_NODE = '0'


class Ant:
    def __init__(self, graph, max_capacity: int, velocity_factor: float):
        self.graph = graph
        self.max_capacity = max_capacity
        self.velocity_factor = velocity_factor

        self.sample_node = lambda nodes: random.choice(nodes)

        self.reset()

    def reset(self):
        self._path = [START_NODE]
        self.capacity = self.max_capacity

        self.pause_ctr = 0

        self.runtime_data = {
            "total_distance": 0,
            "load_history": []
        }

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        if value == START_NODE:
            self.on_visit_start_node()

    def tick(self):
        if self.pause_ctr == 0:
            self.act()

        self.pause_ctr -= 1

    def act(self):
        self.move()
        self.take_item()
        self.set_pause_ctr()

    def move(self):
        current_node = self.path[-1]
        next_node = self.choose_next_node(current_node)

        self.path.append(next_node)

    def take_item(self):
        node = self.path[-1]

        if node == START_NODE:
            return

        load = min(self.capacity, self.graph.nodes[node]['weight'])

        self.capacity -= load
        self.graph.nodes[node]['weight'] -= load

    def set_pause_ctr(self):
        current_node, next_node = self.path[-2], self.path[-1]
        distance = self.graph.get_edge_data(
            current_node, next_node)['weight']

        self.pause_ctr = max(math.ceil(distance * self.velocity_factor), 1)

        self.runtime_data['total_distance'] += distance

    def choose_next_node(self, current_node):
        if self.capacity <= 0:
            return START_NODE

        available_nodes = [
            node for node in self.graph.neighbors(current_node)
            if self.graph.nodes[node]['weight'] > 0
        ]
        if not available_nodes:
            return START_NODE

        return self.sample_node(available_nodes)

    def on_visit_start_node(self):
        total_load = self.max_capacity - self.capacity
        self.runtime_data['load_history'].append(total_load)

        self.capacity = self.max_capacity
