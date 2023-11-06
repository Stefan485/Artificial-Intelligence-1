from problem_definition import *
from search_algorithms.problem import * 
from search_algorithms.gbfs import *
from search_algorithms.astar import *

def solve(initial_state, problem, algorithm):
    print(f"Running {algorithm.__class__.__name__} algorithm...")
    state = initial_state
    for action in algorithm.search():
        print(f"{state} -> h={problem.heuristic_function.h(state)}")
        print(action)
        state = problem.result_function.result(state, action)
    print(state)
    print(f"Number of explored states: {algorithm.num_of_explored}")

if __name__ == "__main__":
    initial_word = input("Initial word: ")
    goal_word = input("Goal word: ")
    initial_state = WordState(initial_word)
    actions_function = WordActionsFunction()
    result_function = WordResultFunction()
    goal_test_function = WordGoalTestFunction(goal_word)
    step_cost_function = WordStepCostFunction()
    heuristic_function = WordHeuristicFunction(goal_word)
    problem = Problem(initial_state=initial_state, 
                      actions_function=actions_function,
                      result_function=result_function,
                      goal_test_function=goal_test_function,
                      step_cost_function=step_cost_function,
                      heuristic_function=heuristic_function)
    gbfs = GBFS(problem)
    astar = AStar(problem)
    solve(initial_state, problem, gbfs)
    print("--------------------------------------------------")
    solve(initial_state, problem, astar)