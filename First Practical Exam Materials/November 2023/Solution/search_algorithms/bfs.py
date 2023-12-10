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
        closest_distance = float("inf")
        closest_node = None
    
        while len(frontier) > 0:
            node = frontier.popleft()
            explored.add(node.state)

            distance_to_goal = node.state.board.manhattan_distance()
            if distance_to_goal < closest_distance:
                closest_distance = distance_to_goal
                closest_node = node

            for action in self.problem.actions_function.actions(node.state):
                child = Node(self.problem.result_function.result(node.state, action), node, action)
                if child.state not in explored and child.state not in map(lambda n: n.state, frontier):
                    if self.problem.goal_test.is_goal_state(child.state):
                        return self.solution(child)
                    frontier.append(child)
                   
        # this is the failure case (goal state is impossible to reach)
        return self.solution(closest_node) if closest_node is not None else None