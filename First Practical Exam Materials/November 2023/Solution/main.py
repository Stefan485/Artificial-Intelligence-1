from board import RotatingnMazeBoard
from problem_definition import RotatingMazeState, RotatingMazeAction, RotatingMazeActionsFunction, \
                        RotatingMazeResultFunction, RotatingMazeGoalTestFunction, RotatingMazeStepCostFunction
from search_algorithms.problem import Problem
from search_algorithms.bfs import BFS
from examples import boards

if __name__ == '__main__':
    board = boards[0]
    initial_state = RotatingMazeState(board)
    actions_function = RotatingMazeActionsFunction()
    result_function = RotatingMazeResultFunction()
    goal_test_function = RotatingMazeGoalTestFunction()
    step_cost_function = RotatingMazeStepCostFunction()
    problem = Problem(initial_state, actions_function, result_function, goal_test_function, step_cost_function)
    bfs = BFS(problem)
    solution = bfs.search()
    state = initial_state
    print(state)
    for action in solution:
        print(action)
        state = result_function.result(state, action)
        print(state)
    print(f"Number of steps: {len(solution)}")
    