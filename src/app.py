from pathlib import Path
from typing import List
import numpy as np
import networkx as nx
import json
import matplotlib.pyplot as plt
from algorithms.interface import Order
from objects.robot import Robot, RobotSize
from objects.warehouse import Warehouse
from algorithms.genetics.other import generate_random_solution
from algorithms.genetics.genetic import GeneticAlgorithm
from algorithms.swarm import AntAlgorithm
import argparse

INPUT_DATA_DIR = Path('C:\\Users\\arkre\\OneDrive\\Pulpit\\deep_learning\\input_data')

def test_genetic(selection_method: str, iterations_number: int, population: int):
    with open(INPUT_DATA_DIR / 'robots/robotsg2.json', 'r') as f:
        sizes = json.load(f)
    print(f"sizes:{sizes}")
    with open(INPUT_DATA_DIR / 'orders/order2.json', 'r') as f:
        order = json.load(f)
    print(f"order:{order}")
    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')
    print(f"graph:{graph}")
    robots = [
        Robot(f'{i+1}', size)
        for i, size in enumerate(sizes)
    ]
    print(f"robots:{robots[0]}")
    warehouse = Warehouse(graph, robots)
    print(f"warehouse:{warehouse.robots[0]}")
    order = {int(k): v for k, v in order.items()}
    print(f"order:{order}")
    warehouse.graph = nx.relabel_nodes(warehouse.graph, {n: int(n) for n in warehouse.graph})
    print(f"warehouse.graph:{warehouse.graph}")
    GeneticAlg = GeneticAlgorithm(Order(order), warehouse, selection_method)
    print(f"Order(order): {Order(order)}")
    GeneticAlg.run(max_iter=iterations_number, population_count=population)
    print("---------------------------")
    print(f"selection: {selection_method}, iterations: {iterations_number}, population: {population}")

    # longest = calculate_one(solution, warehouse)
    # print(GeneticAlg.best_solution)    
    x_vec = np.linspace(1, len(GeneticAlg.best_list), len(GeneticAlg.best_list))

    plt.step(x_vec, GeneticAlg.best_list, color='b', linestyle='-')
    plt.title('Step Plot of Change of Cost Function', fontsize=14)
    plt.xlabel('Iteration', fontsize=12)
    plt.ylabel('Value of Cost Function', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(['Cost Function'], loc='best', fontsize=10)
    plt.tight_layout() 
    plt.show()

    # return list_best

def test_case_1():
    with open(INPUT_DATA_DIR / 'robots\\robots1.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders\\order1.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs\\10_10.adjlist')

    robots = [
        Robot(f'{i+1}', size)
        for i, size in enumerate(sizes)
    ]
    warehouse = Warehouse(graph, robots)
    order = {int(k): v for k, v in order.items()}

    alg = AntAlgorithm.from_input_data(order, warehouse)
    alg.solve(
        iter=1000,
        alpha=0.1,
        beta=0.1,
        decay_rate=0.01
    )

    # here will be generating plots script etc.

    return alg


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enter flags for various algorithms fields:")
    parser.add_argument('-s', '--selection', choices=['rank', 'tournament', 'roulette', 'proportional'], default='rank', help='Selection method')
    parser.add_argument('-i', '--iterations', default=100, type=int, help='Iteratiions number of genetic algorithm')
    parser.add_argument('-p', '--population', default=10, type=int, help='Initial population size')
    args = parser.parse_args()
    test_genetic(args.selection, args.iterations, args.population)
    # test_case_1()
