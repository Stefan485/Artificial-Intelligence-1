from problem_definition import EightPuzzleState, EightPuzzleAction, EightPuzzleActionsFunction, EightPuzzleResultFunction, \
                               EightPuzzleGoalTestFunction, EightPuzzleStepCostFunction, EightPuzzleHeuristic
from search_algorithms.problem import Problem
from board import EightPuzzleBoard
from search_algorithms.gbfs import GBFS
from search_algorithms.astar import AStar
from search_algorithms.search import Search

def solve(algorithm: Search):
    print(f"Running {algorithm.__class__.__name__} algorithm...")
    state = algorithm.problem.initial_state
    actions, num_explored_states = algorithm.search()
    for i, action in enumerate(actions):
        print(state)
        print(f"Action {i+1}: {action}")
        new_state = result_function.result(state, action)
        state = new_state
    print(state)
    print(f"Number of actions: {len(actions)}")
    print(f"Number of explored states: {num_explored_states}")

if __name__ == "__main__":
    table = [[5, 4, 0], [6, 1, 8], [7, 3, 2]]
    board = EightPuzzleBoard(table, 3, 3)
    initial_state = EightPuzzleState(board)
    actions_function = EightPuzzleActionsFunction()
    result_function = EightPuzzleResultFunction()
    goal_test = EightPuzzleGoalTestFunction()
    step_cost_function = EightPuzzleStepCostFunction()
    heuristic = EightPuzzleHeuristic()

    problem = Problem(initial_state, actions_function, result_function, goal_test, step_cost_function, heuristic)
    gbfs = GBFS(problem)
    astar = AStar(problem)
    solve(gbfs)
    print(50 * "-")
    solve(astar)
        