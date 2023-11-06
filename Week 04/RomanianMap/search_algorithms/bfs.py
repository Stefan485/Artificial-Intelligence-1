from typing import List
from collections import deque

from .search import Search
from .interfaces import Action
from .node import Node

class BFS(Search):
    """Solves search problem using BFS algorithm."""

    def __init__(self, problem):
        self.problem = problem

    def search(self) -> List[Action]:
        node = Node(self.problem.initial_state)
        if self.problem.goal_test.is_goal_state(node.state):
            return []
        frontier = deque([node])
        explored = set()
    
        while len(frontier) > 0:
            node = frontier.popleft()
            explored.add(node.state)
            for action in self.problem.actions_function.actions(node.state):
                child = Node(self.problem.result_function.result(node.state, action), node, action)
                if child.state not in explored and child.state not in map(lambda n: n.state, frontier):
                    if self.problem.goal_test.is_goal_state(child.state):
                        return self.solution(child)
                    frontier.append(child)
                   
        # this is the failure case (goal state is impossible to reach)
        return None