from objects import Robot, Warehouse
from plots import plot_loss_fn, plot_all_robot_paths
from algorithms.swarm import AntAlgorithm
import json
from pathlib import Path
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')


INPUT_DATA_DIR = Path('/app/input_data')


def test_case_1():
    with open(INPUT_DATA_DIR / 'robots/robots1.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order1.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

    return sizes, order, graph

def test_case_2():
    with open(INPUT_DATA_DIR / 'robots/robots2.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order1.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

    return sizes, order, graph

def test_case_3():
    with open(INPUT_DATA_DIR / 'robots/robots3.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order1.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

    return sizes, order, graph


def test_case_4():
    with open(INPUT_DATA_DIR / 'robots/robots4.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order2.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

    return sizes, order, graph


def test_case_5():
    with open(INPUT_DATA_DIR / 'robots/robots5.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order2.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

    return sizes, order, graph

def test_case_6():
    with open(INPUT_DATA_DIR / 'robots/robots6.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order2.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

    return sizes, order, graph

def main(test_case, index):
    
    sizes, order, graph = test_case()

    robots = [
        Robot(f'{i+1}', size)
        for i, size in enumerate(sizes)
    ]
    warehouse = Warehouse(graph, robots)
    order = {int(k): v for k, v in order.items()}

    alg = AntAlgorithm.from_input_data(order, warehouse)
    solution = alg.solve(
        iter=1000,
        alpha=0.1,
        beta=0.1,
        decay_rate=0.01
    )

    plot_all_robot_paths(solution, alg.graph, index)
    plot_loss_fn(alg.runtime_data, index)

    return alg


if __name__ == '__main__':
    main(test_case_1, 1)
    main(test_case_2, 2)
    main(test_case_3, 3)
    main(test_case_4, 4)
    main(test_case_5, 5)
    main(test_case_6, 6)
