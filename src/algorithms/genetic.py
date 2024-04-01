import random

from genetics.operators import crossover, mutate
from genetics.other import generate_population, calculate_all, rank_selection,\
    calculate_one, parents_to_population_rate


class GeneticAlgorithm:
    def __init__(self, order, warehouse, population=None) -> None:
        self.order = order
        self.warehouse = warehouse
        self.population = population  # [(AlgorithmOutput, cost)]
        self.weights = {}  # {item: weight}
        self.best_solution = ()  # (solution, cost)

    def run(self, max_iter, population_count, mutation_rate=0.2):
        if self.population is None:
            self.population = []
            population = generate_population(population_count)
            costs = calculate_all(population)
            for i in range(len(population)):
                self.population.append((population[i], costs[i]))

        self.population.sort(key=lambda tup: tup[1])
        for i in range(max_iter):
            self.single_iteration(mutation_rate)
            if self.best_solution == () or self.best_solution[1] > self.population[0][1]:
                self.best_solution = self.population[0]

        return self.best_solution

    def single_iteration(self, mutation_rate):
        temp_population = self.population[:len(self.population) * parents_to_population_rate]
        to_crossover = rank_selection(self.population)
        for j in range(len(to_crossover)):
            parents = random.sample(to_crossover, 2)
            to_crossover.remove(parents[0])
            to_crossover.remove(parents[1])
            # crossover
            child = crossover(parents[0], parents[1], self.order, self.weights)

            # mutation
            if random.randrange(0, 1) < mutation_rate:
                mutate(child, len(child.result) // 2 + 1)  # can be changed

            cost = calculate_one(child)
            temp_population.append((child, cost))
            temp_population.sort(key=lambda tup: tup[1])
            self.population = temp_population


# testy TODO: ogarnac strukture zeby miec wieght dict oraz wiedziec jak obliczac koszty sciezek
import networkx as nx


START_NODE = '0'
graph = nx.read_adjlist('/content/graph_4_4.adjlist')
G = nx.path_graph(graph)  # or DiGraph, MultiGraph, MultiDiGraph, etc
points = [{n: list(nbrdict.keys())} for n, nbrdict in G.adjacency()]

shortest_paths = nx.shortest_path(graph)

orders = {
    7: 1,
    11: 1,
    9: 3,
    8: 1,
    6: 12,
    1: 4,
    2: 2,
}
nodes = list(orders.keys())
nodes = [START_NODE] + [str(node) for node in nodes]
complete_graph = nx.Graph()

for src in nodes:
    for dst in nodes:
        if src == dst:
            continue
        path = shortest_paths[src][dst]
        complete_graph.add_edge(src, dst, weight=len(path)-1, path=path, sum_load=0, feromone=0)



nx.set_node_attributes(complete_graph, {
    node: {"weight": orders.get(int(node), np.inf)}
    for node in nodes
})
list(complete_graph.nodes())