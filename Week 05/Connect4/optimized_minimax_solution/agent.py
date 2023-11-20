from abc import ABC, abstractmethod

from game_algorithms.interfaces import GameState, Action
from game_definition import Connect4State, Connect4Action, Connect4ActionsFunction

class Agent:
    def __init__(self, game, mark, name):
        self.game = game
        self.mark = mark
        self.name = name

    @abstractmethod
    def make_move(self, game_state: GameState) -> Action:
        """Returns the action that the agent should take.
        Args:
            game_state (GameState): The current game state.
        Returns:
            Action: The action that the agent should take.
        """
        pass

    def __str__(self) -> str:
        return self.name

class Human(Agent):
    def __init__(self, game, mark, name):
        super().__init__(game, mark, name)

    def make_move(self, game_state: GameState) -> Action:
        """Returns the action that the agent should take.
        Args:
            game_state (GameState): The current game state.
        Returns:
            Action: The action that the agent should take.
        """
        available_columns = [action.column for action in self.game.actions_function.actions(game_state)]
        column = -1
        while column not in available_columns:
            print(f"Enter the column where you want to put your mark {available_columns}")
            column = int(input())
            if column not in available_columns:
                print("Invalid column")

        return Connect4Action(column, self.mark)

    
class AI(Agent):
    def __init__(self, game, mark, name):
        super().__init__(game, mark, name)

    def make_move(self, game_state: GameState) -> Action:
        """Returns the action that the agent should take.
        Args:
            game_state (GameState): The current game state.
        Returns:
            Action: The action that the agent should take.
        """
        return self.game.minimax_decision(game_state)
