from search_algorithms.interfaces import State, Action, ActionsFunction, ResultFunction, GoalTestFunction, StepCostFunction, HeuristicFunction
from board import EightPuzzleBoard

class EightPuzzleState(State):
    def __init__(self, board: EightPuzzleBoard):
        self.board = board

    def __str__(self):
        return str(self.board)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))
    
class EightPuzzleAction(Action):
    def __init__(self, direction):
        assert direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.direction = direction

    def __str__(self):
        return self.direction
    
class EightPuzzleActionsFunction(ActionsFunction):
    def actions(self, state):
        actions = []
        i, j = state.board.get_blank_position()
        num_rows, num_columns = state.board.get_board_dimensions()
        if i > 0:
            actions.append(EightPuzzleAction('UP'))
        if i < num_rows - 1:
            actions.append(EightPuzzleAction('DOWN'))
        if j > 0:
            actions.append(EightPuzzleAction('LEFT'))
        if j < num_columns - 1:
            actions.append(EightPuzzleAction('RIGHT'))
        return actions
    
class EightPuzzleResultFunction(ResultFunction):
    def __swap_values(self, board: EightPuzzleBoard, i1: int, j1: int, i2: int, j2: int):
        value1 = board.get_value(i1, j1)
        value2 = board.get_value(i2, j2)
        board.set_value(i1, j1, value2)
        board.set_value(i2, j2, value1)

    def result(self, state: State, action: Action) -> State:
        new_board = state.board.clone()
        i, j = new_board.get_blank_position()
        if action.direction == 'UP':
            self.__swap_values(new_board, i, j, i-1, j)
        elif action.direction == 'DOWN':
            self.__swap_values(new_board, i, j, i+1, j)
        elif action.direction == 'LEFT':
            self.__swap_values(new_board, i, j, i, j-1)
        elif action.direction == 'RIGHT':
            self.__swap_values(new_board, i, j, i, j+1)
        return EightPuzzleState(new_board)
    
class EightPuzzleGoalTestFunction(GoalTestFunction):
    def is_goal_state(self, state: State):
        goal_board = EightPuzzleBoard.create_goal_board(*state.board.get_board_dimensions())
        return state.board == goal_board
    
class EightPuzzleStepCostFunction(StepCostFunction):
    def cost(self, state: State, action: Action, state1: State) -> float:
        return 1
    
class EightPuzzleHeuristic(HeuristicFunction):
    def h(self, state: State) -> float:
        goal_board = EightPuzzleBoard.create_goal_board(*state.board.get_board_dimensions())
        manhattan_distance_sum = 0
        positions = state.board.get_positions_for_each_tile()
        goal_positions = goal_board.get_positions_for_each_tile()
        for tile in positions:
            manhattan_distance_sum += abs(positions[tile][0] - goal_positions[tile][0]) + abs(positions[tile][1] - goal_positions[tile][1])
        return manhattan_distance_sum

      
    

    


    