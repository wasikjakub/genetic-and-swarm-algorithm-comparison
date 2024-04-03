from typing import Dict, List, Literal, NamedTuple

from objects import Robot, Warehouse

NodeId = str


class Order(NamedTuple):
    # int is the number of items in a given node
    items: Dict[NodeId, int]


class RobotRoute(NamedTuple):
    route: List[NodeId]
    # items to pick on a route
    items: Dict[NodeId, int]


class Node(NamedTuple):
    id: int
    weight: int


class AlgorithmInput(NamedTuple):
    warehouse: Warehouse
    order: Order


class AlgorithmOutput(NamedTuple):
    result: Dict[Robot, RobotRoute]
