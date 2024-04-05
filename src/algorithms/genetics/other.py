import networkx as nx
import numpy as np
import random
from objects.robot import Robot
from algorithms.interface import AlgorithmOutput, Order, RobotRoute
from typing import Dict, List
from objects.warehouse import Warehouse
from collections import defaultdict

from algorithms.genetics.transform_graph import change_graph

def fill_routes(solution: AlgorithmOutput, items_left: Order, weights: Dict[int, int]):
    for i, quantity in items_left.items.items():
        times = calculate_times(solution.result)
        subtracted = 0
        for k in range(len(times)):
            temp_robot = min(times, key=times.get)
            times.pop(temp_robot)
            temp_cap = capacity_left(temp_robot, solution.result[temp_robot], weights)
            if temp_cap > 0:
                if temp_cap < weights[i] * (quantity-subtracted):
                    for j in range(quantity-subtracted):
                        if capacity_left(temp_robot, solution.result[temp_robot], weights) > weights[i]:
                            if i in solution.result[temp_robot].route:
                                solution.result[temp_robot].items[i] += 1
                            else:
                                solution.result[temp_robot].route.append(i)
                                solution.result[temp_robot].items[i] = 1
                            subtracted += 1
                else:
                    if i in solution.result[temp_robot].route:
                        solution.result[temp_robot].items[i] += quantity - subtracted
                    else:
                        solution.result[temp_robot].route.append(i)
                        solution.result[temp_robot].items[i] = quantity - subtracted
                    subtracted += quantity - subtracted

            if items_left.items[i] == subtracted:
                break


def capacity_left(robot: Robot, route: RobotRoute, weights: Dict[int, int]) -> int:
    s = 0
    for i, quantity in route.items.items():
        s += weights[i] * quantity  # I need this weights dict that says which item weighs how much
    return robot.load_capacity - s


def rank_selection(population: List[AlgorithmOutput, int]) -> List[AlgorithmOutput]:  # or double
    solutions_to_take = int(len(population) * parents_to_population_rate)  # I want to take 2/3 of the solutions

    return [solution[0] for solution in population[:solutions_to_take]]


def calculate_times(robots: Dict[Robot, RobotRoute]) -> Dict[Robot, int]:
    #TODO calculate costs of routes for each robot
    l = list(robots.keys())
    return {l[i]: i*2 for i in range(len(robots))}  # dummy


def calculate_one(solution: AlgorithmOutput) -> int:
    #TODO: najdłuższa z calculate_times
    pass


def calculate_all(population: List[AlgorithmOutput]) -> List[int]:  # albo double
    #TODO wykonać calculate_times na wszystkich osobnikach
    pass

def generate_random_solution(orders: Dict, warehouse: Warehouse) -> AlgorithmOutput:
    solution = defaultdict(lambda: RobotRoute([], {}))

    graph = warehouse.graph
    robot_list = warehouse.robots

    picked_items = set()  #track picked items

    for robot in robot_list:
        route = ['0']  #starting point for each robot
        items = {}  #tracking gathered items
        curr_capacity = robot.load_capacity

        for _ in range(len(orders)):
            if curr_capacity <= 0:
                break

            #filter out items that have already been picked
            available_items = [item_id for item_id in orders.keys() if item_id not in picked_items and orders[item_id] > 0]

            if not available_items:
                break

            item_id = random.choice(available_items)  #random item to pick up

            shortest_paths = nx.shortest_path(graph, route[-1], str(item_id))
            route.extend(shortest_paths[1:])

            amount_to_pick = min(orders[item_id], curr_capacity)
            items[str(item_id)] = amount_to_pick
            curr_capacity -= amount_to_pick
            orders[item_id] -= amount_to_pick

            #track picked items
            picked_items.add(item_id)

        shortest_paths = nx.shortest_path(graph, route[-1], '0') #return to starting point
        route.extend(shortest_paths[1:])

        solution[robot] = RobotRoute(route=route, items=items)

    return solution

def generate_population(count: int) -> List[AlgorithmOutput]:
    return [generate_random_solution() for i in range(count)]


parents_to_population_rate = 2 / 3
