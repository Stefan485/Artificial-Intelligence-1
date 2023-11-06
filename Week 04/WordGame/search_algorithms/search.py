from abc import ABC, abstractmethod
from typing import List

from .problem import Problem
from .interfaces import Action
from .node import Node

class Search(ABC):
    """This class defines uninformed search algorithms."""

    def __init__(self, problem: Problem):
        """Initialize the uninformed search algorithm.
        Args:
            problem (Problem): The problem.
        """
        assert isinstance(problem, Problem), "The problem must be an instance of Problem"
        self.problem = problem

    @abstractmethod
    def search(self) -> List[Action]:
        """Search for a solution of the problem.
        Returns:
            List[Action]: List of actions to reach the goal.
        """
        pass

    def solution(self, goal_node: Node) -> List[Action]:
        """Returns all actions that agent needs to perform to reach the goal.
        Args:
            goal_node (Node): The goal node from the graph search.
        Returns:
            List[Action]: List of actions to reach the goal.
        """
        actions = []
        node = goal_node
        while node.parent_node is not None:
            actions.append(node.action)
            node = node.parent_node
        actions.reverse()
        return actions
      