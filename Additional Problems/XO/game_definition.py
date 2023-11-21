from typing import List
from game_algorithms.interfaces import GameState, Action, ActionsFunction, ResultFunction
from game_algorithms.game import Game
from board import XOBoard

class XOState(GameState):
    def __init__(self, state: XOBoard, player_to_move: str):
        return super().__init__(state, player_to_move)
    
class XOAction(Action):
    def __init__(self, row, column, mark):
        self.row = row
        self.column = column
        self.mark = mark

    def __str__(self):
        return f"Action: Put {self.mark} in row {self.row} and column {self.column}"
    
    def field_position(self):
        return f"({self.row}, {self.column})"
    
class XOActionsFunction(ActionsFunction):
    def actions(self, game_state: XOState) -> List[Action]:
        actions = []
        for row in range(game_state.state.num_rows):
            for column in range(game_state.state.num_columns):
                if game_state.state.board[row][column] == " ":
                    actions.append(XOAction(row, column, game_state.player_to_move))
        return actions
    
class XOResultFunction(ResultFunction):
    def result(self, game_state: XOState, action: Action) -> XOBoard:
        new_state = game_state.state.clone()
        new_state.set_value(action.row, action.column, game_state.player_to_move)
        new_player_to_move = "O" if game_state.player_to_move == "X" else "X"
        return XOState(new_state, new_player_to_move)
    
class XOGame(Game):
    def compute_utility(self, game_state: GameState) -> float:
        if game_state.state.check_win("X"):
            return 1
        elif game_state.state.check_win("O"):
            return -1
        else:
            return 0
    
    def is_terminal(self, game_state: GameState) -> bool:
        return game_state.state.is_terminal()