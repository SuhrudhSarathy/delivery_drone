"""Astar planner for planning in 3D. This needs an input of nodes Assuming that there is no collision"""
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

        self.g = np.inf
        self.h = np.inf
        self.f = np.inf

        self.parent = None

        self.adjacent_nodes = []
        
    def __eq__(self, obj: object)->bool:
        return obj.x == self.x and obj.y == self.y and obj.z == self.z

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"
    
    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"

class AStar:
    def __init__(self, use_heuristic=False, heuristic_weight=1.0, plot=False):
        self.use_heuristic = use_heuristic
        self.heurisitic_weight = heuristic_weight
        self.plot = plot

        self.nodes = []

        self.goal = None

    def add_nodes(self, nodes: list)->None:
        self.nodes = [Node(node[0], node[1], node[2]) for node in nodes]

    def search(self, start: list, goal: list):
        """Main AStar Algorithm"""
        assert len(self.nodes) != 0, "Add nodes to search"
        self.goal = Node(goal[0], goal[1], goal[2])

        self.open_nodes = []
        start = Node(start[0], start[1], start[2])

        start.g = 0
        start.h = self.heuristic(start)
        start.f = start.g + start.h

        self.open_nodes.append(start)

        while len(self.open_nodes) != 0:
            current = sorted(self.open_nodes, key=lambda x:x.f)[0]
            
            self.open_nodes.pop(0)

            if current == self.goal:
                return True, self.backtrack(current)

            # Find all the adjacent nodes for the node current
            self.find_adjacent_nodes(current)

            for node in current.adjacent_nodes:

                if node.f > current.f + self.cost(current, node):
                    node.g = current.g + self.cost(current, node)
                    node.h = self.heuristic(node)
                    node.f = node.g + self.heurisitic_weight * node.h

                    node.parent = current

                    if node not in self.open_nodes:
                        self.open_nodes.append(node)

        return False, []

    #-- Helper functions
    def cost(self, node1: Node, node2: Node)->float:
        X = node2.x - node1.x
        Y = node2.y - node1.y
        Z = node2.z - node1.z

        return sqrt(X**2 + Y**2 + Z**2)

    def heuristic(self, node: Node)->float:
        return self.cost(self.goal, node)

    def backtrack(self, node: Node)->list:
        print("Backtracking..")
        current = node
        path = [current]
        while current.parent is not None:
            path.append(current.parent)
            current = current.parent

        return path[::-1]

    def find_adjacent_nodes(self, node: Node):
        nodes = self.nodes.copy()
        nodes.remove(node)
        nodes = sorted(nodes, key=lambda x: self.cost(x, node))
        node.adjacent_nodes = []
        for i in range(3):
            node.adjacent_nodes.append(nodes[i])
