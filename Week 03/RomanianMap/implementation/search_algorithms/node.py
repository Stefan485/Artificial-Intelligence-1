from typing import Optional
from abc import ABC, abstractmethod

from .interfaces import State, Action

class Node:
    """This class represents a node in a search tree."""

    def __init__(self, state: State, parent_node = None, action: Optional[Action] = None):
        """Initialize the node.
        Args:
            state (State): The current state.
            parent_node (Node): The parent node in the search tree (root has value None).
            action (Action): The action that was applied to the parent node to get to this node.
            step_cost (float): The cost of the step from the parent node to this node.
        """
        self.state = state
        self.parent_node = parent_node
        self.action = action

    def __lt__(self, other):
        raise NotImplementedError

class UCSNode(Node):
    def __init__(self, state: State, parent_node = None, action: Optional[Action] = None, step_cost: Optional[float] = 0):
        super().__init__(state, parent_node, action)
        self.path_cost = parent_node.path_cost + step_cost if parent_node is not None else step_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost 
    