from objects import Robot, Warehouse
from plots import plot_loss_fn, plot_all_robot_paths
from algorithms.swarm import AntAlgorithm
import json
from pathlib import Path
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')


INPUT_DATA_DIR = Path('/app/input_data')

def test_case(link_to_robots, link_to_orders, link_to_graph='graphs/10_10.adjlist'):
    with open(INPUT_DATA_DIR / link_to_robots, 'r') as f:
        sizes = json.load(f)

    with open(INPUT_DATA_DIR / link_to_orders, 'r') as f:
        order = json.load(f)

    graph = nx.read_adjlist(INPUT_DATA_DIR / link_to_graph)

    return sizes, order, graph

def main(test_case, index, link_to_robots, link_to_orders):
    
    sizes, order, graph = test_case(link_to_robots, link_to_orders)

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
    test_robots = ['robots/robots1.json', 'robots/robots2.json', 'robots/robots3.json', 'robots/robots4.json', 'robots/robots5.json', 'robots/robots6.json']
    test_orders = ['orders/order1.json', 'orders/order1.json', 'orders/order1.json', 'orders/order2.json', 'orders/order2.json', 'orders/order2.json']
    for i in range(6):
        main(test_case=test_case, index=i+1, link_to_robots=test_robots[i], link_to_orders=test_orders[i])
    
