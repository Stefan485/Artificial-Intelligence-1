from typing import List
import heapq

from .search import Search
from .interfaces import Action
from .node import UCSNode

class UCS(Search):
    """Solves search problem using UCS algorithm."""

    def __init__(self, problem):
        self.problem = problem

    def search(self) -> List[Action]:
        node = UCSNode(self.problem.initial_state)
        if self.problem.goal_test.is_goal_state(node.state):
            return []
        frontier = []
        heapq.heappush(frontier, node)
        explored = set()
    
        while frontier:
            node = heapq.heappop(frontier)
            if self.problem.goal_test.is_goal_state(node.state):
                return self.solution(node)
            explored.add(node.state)
            for action in self.problem.actions_function.actions(node.state):
                child_state = self.problem.result_function.result(node.state, action)
                child = UCSNode(child_state, node, action, self.problem.step_cost_function.cost(node.state, action, child_state))
                if child.state not in explored:
                    heapq.heappush(frontier, child)
                   
        # this is the failure case (goal state is impossible to reach)
        return None