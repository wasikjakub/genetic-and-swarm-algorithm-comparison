import json
from pathlib import Path
import networkx as nx

from algorithms.swarm import AntAlgorithm
from objects import Robot, Warehouse

INPUT_DATA_DIR = Path('../input_data')


def test_case_1():
    with open(INPUT_DATA_DIR / 'robots/robots1.json', 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / 'orders/order1.json', 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / 'graphs/10_10.adjlist')

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
