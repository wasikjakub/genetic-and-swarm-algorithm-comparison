import networkx as nx
from pathlib import Path
from typing import List
from robot import Robot

class Warehouse:
    def __init__(self, txt_file: Path, robots: List[Robot]) -> None:
        self.graph = nx.read_adjlist(txt_file)
        self.robots = robots
