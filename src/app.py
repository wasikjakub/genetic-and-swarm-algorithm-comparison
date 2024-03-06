# import warehouse
# import robot
# import node

import random 
import networkx as nx

def order(num_items):
    #TODO zwrócić listę zamówień {id: licza sztuk, id2: liczba sztuk, ...}

    product_ids = [f'id{i+1}' for i in range(num_items)]
    
    quantities = [1, 2, 3, 4, 5]
    weights = [0.2, 0.3, 0.25, 0.15, 0.1]  # Adjust weights as needed

    orders = {product_id: random.choices(quantities, weights, k=1)[0] for product_id in product_ids}

    return orders

def graph():
    G = nx.Graph()

    G.add_node(1, weight=10)
    G.add_node(2, weight=15)
    G.add_node(3, weight=20)

    G.add_edge(1, 2, weight=5)
    G.add_edge(2, 3, weight=7)
    G.add_edge(1, 3, weight=9)
    
    return G
def generate_robots():
    #TODO zwrócić listę robotów {robot1, robot2, ...}
    raise NotImplementedError

def main():
    print("Hello World!")
    #TODO generacja magazynu i robotów
    warehouse = warehouse.Warehouse()
    robots = generate_robots()
    #TODO wygenerowanie listy zamówień 
    orders = order()

    #TODO run algorithm (rojowy lub genetyczny)
    algorithm = algorithm(order=orders, warehouse=warehouse, 
                          robots=robots) #TODO zwrócić listę tras i kosztów
    #TODO wizualizacja wyników i porównanie z innymi algorytmami