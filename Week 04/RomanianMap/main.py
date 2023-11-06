from romanian_map import *
from search_algorithms.interfaces import *
from search_algorithms.problem import *
from search_algorithms.dfs import *
from search_algorithms.bfs import *
from search_algorithms.ucs import *
from search_algorithms.gbfs import *
from search_algorithms.astar import *
from problem_definition import *

def solve(algorithm):
    print(f"Running {algorithm.__class__.__name__} algorithm...")
    total_cost = 0
    state = initial_state
    for action in algorithm.search():
        print(action)
        new_state = result_function.result(state, action)
        total_cost += step_cost_function.cost(state, action, new_state)
        state = new_state
    print(f"Total cost of the path: {total_cost}")

if __name__ == "__main__":
    romanian_map = RomanianMap("straight_line_distances.txt", "city_connections.txt")
    initial_state = RomanianMapState("Arad")
    actions_function = RomanianMapActionsFunction(romanian_map.city_connections)
    result_function = RomanianMapResultFunction()
    goal_test = RomanianMapGoalTestFunction()
    step_cost_function = RomanianMapStepCostFunction(romanian_map.city_connections)
    problem = Problem(initial_state, actions_function, result_function, goal_test, step_cost_function)

    solve(DFS(problem))
    solve(BFS(problem))
    solve(UCS(problem))
    heuristic_function = RomanianMapHeuristicFunction(romanian_map.straigth_line_distances)
    problem = Problem(initial_state, actions_function, result_function, goal_test, step_cost_function, heuristic_function)
    solve(GBFS(problem))
    solve(AStar(problem))
    