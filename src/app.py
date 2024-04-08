import random
from pathlib import Path
from typing import List
import networkx as nx
# from algorithms.swarm import AntAlgorithm, transform_graph
# from algorithms.swarm.ant import Ant
from algorithms.interface import Order
from objects.robot import Robot, RobotSize
from objects.warehouse import Warehouse
from algorithms.genetics.other import generate_random_solution, calculate_one
from algorithms.genetics.genetic import GeneticAlgorithm

def order(num_items):
    # TODO zwrócić listę zamówień {id: licza sztuk, id2: liczba sztuk, ...}

    product_ids = [f'id{i+1}' for i in range(num_items)]

    quantities = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.25, 0.15, 0.1]  # Adjust weights as needed

    orders = {product_id: random.choices(quantities, weights, k=1)[
        0] for product_id in product_ids}

    return orders


def generate_robots(size_of_robots: List[RobotSize] = [RobotSize.SMALL, RobotSize.SMALL]):
    tab = []
    for idx, size in enumerate(size_of_robots):
        tab.append(Robot(id=idx, size=size))

    return tab


def mock_main():
    # graph = nx.read_adjlist('generated_graphs\graph_4_4.adjlist')
    path = Path('..\\input_data\\graphs\\4_4.adjlist')

    orders = {
        7: 5,
        11: 4,
        9: 3,
        8: 3,
        6: 2,
        1: 4,
        2: 3,
    }

    robots = [
        Robot('1', RobotSize.SMALL),
        Robot('2', RobotSize.SMALL),
        Robot('3', RobotSize.MEDIUM),
        Robot('4', RobotSize.LARGE),
    ]

    warehouse = Warehouse(
        txt_file=path, robots=robots)
    warehouse.graph = nx.relabel_nodes(warehouse.graph, {n: int(n) for n in warehouse.graph})

    GeneticAlg = GeneticAlgorithm(Order(orders), warehouse)
    GeneticAlg.run(20, 10)

    solution = generate_random_solution(orders, warehouse)

    # longest = calculate_one(solution, warehouse)
    print(GeneticAlg.best_solution)
    print(GeneticAlg.best_list)



if __name__ == '__main__':
    mock_main()
