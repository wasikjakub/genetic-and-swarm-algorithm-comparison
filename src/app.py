from warehouse import Warehouse
from algorithm import algorithm

import random 
import networkx as nx

def order(num_items):
    #TODO zwrócić listę zamówień {id: licza sztuk, id2: liczba sztuk, ...}

    product_ids = [f'id{i+1}' for i in range(num_items)]
    
    quantities = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.25, 0.15, 0.1]  # Adjust weights as needed

    orders = {product_id: random.choices(quantities, weights, k=1)[0] for product_id in product_ids}

    return orders


def generate_robots():
    #TODO zwrócić listę robotów {robot1, robot2, ...}
    raise NotImplementedError

def main():
    print("Hello World!")
    #TODO generacja magazynu i robotów

    warehouse = Warehouse()
    robots = generate_robots()
    #TODO wygenerowanie listy zamówień 
    orders = order()

    #TODO run algorithm (rojowy lub genetyczny)
    result = algorithm(order=orders, warehouse=warehouse) #TODO zwrócić listę tras i kosztów
    #TODO wizualizacja wyników i porównanie z innymi algorytmami