from objects.robot import Robot
from objects.warehouse import Warehouse
from algorithms.interface import RobotSize
from algorithms.swarm import AntAlgorithm

import random 
import networkx as nx
from typing import List

def order(num_items):
    #TODO zwrócić listę zamówień {id: licza sztuk, id2: liczba sztuk, ...}

    product_ids = [f'id{i+1}' for i in range(num_items)]
    
    quantities = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.25, 0.15, 0.1]  # Adjust weights as needed

    orders = {product_id: random.choices(quantities, weights, k=1)[0] for product_id in product_ids}

    return orders

def generate_robots(size_of_robots: List[RobotSize] = [RobotSize.SMALL, RobotSize.SMALL]):
    tab = []
    for idx, size in enumerate(size_of_robots):
        tab.append(Robot(id=idx, size=size))

    return tab

def main():
    print("Hello World!")
    #TODO generacja magazynu i robotów
    size_of_robots = [RobotSize.SMALL, RobotSize.SMALL]   # TODO: zparametryzować
    robots = generate_robots(size_of_robots)
    warehouse = Warehouse(txt_file='generated_graphs/graph_4_4.adjlist', robots=robots)
    #TODO wygenerowanie listy zamówień 
    orders = order()

    #TODO run algorithm (rojowy lub genetyczny)
    result = AntAlgorithm(order=orders, warehouse=warehouse) #TODO zwrócić listę tras i kosztów
    #TODO wizualizacja wyników i porównanie z innymi algorytmami


main()