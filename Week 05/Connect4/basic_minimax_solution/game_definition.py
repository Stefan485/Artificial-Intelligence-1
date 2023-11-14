from typing import List
from game_algorithms.interfaces import GameState, Action, ActionsFunction, ResultFunction
from game_algorithms.game import Game
from board import Connect4Board

class Connect4State(GameState):
    def __init__(self, state: Connect4Board, player_to_move: str):
        return super().__init__(state, player_to_move)

class Connect4Action(Action):
    def __init__(self, column, mark):
        self.column = column
        self.mark = mark

    def __str__(self):
        return f"Action: Put mark {self.mark} in column {self.column}"
    
class Connect4ActionsFunction(ActionsFunction):
    def actions(self, game_state: Connect4State) -> List[Action]:
        actions = []
        for column in range(game_state.state.board_size[1]):
            if game_state.state.board[game_state.state.board_size[0] - 1][column] == " ":
                actions.append(Connect4Action(column, game_state.player_to_move))
        return actions
    
class Connect4ResultFunction(ResultFunction):
    def result(self, game_state: Connect4State, action: Action) -> Connect4Board:
        new_state = game_state.state.clone()
        for row in range(new_state.board_size[0]):
            if new_state.board[row][action.column] == " ":
                new_state.board[row][action.column] = game_state.player_to_move
                break
        new_player_to_move = "O" if game_state.player_to_move == "X" else "X"
        return Connect4State(new_state, new_player_to_move)
    
class Connect4Game(Game):
    def compute_utility(self, game_state: Connect4State) -> float:
        return game_state.state.heuristic_evaluation()
    
    def is_terminal(self, game_state: Connect4State) -> bool:
        return game_state.state.is_terminal()

    
