from abc import ABC, abstractmethod

from game_algorithms.interfaces import GameState, Action
from game_definition import XOAction

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
        available_actions = [(action.row, action.column) for action in self.game.actions_function.actions(game_state)]
        print(f"Available moves: {available_actions}")
        while True:
            row, column = int(input("Enter row: ")), int(input("Enter column: "))
            if (row, column) in available_actions:
                return XOAction(int(row), int(column), self.mark)
            else:
                print("Invalid move. Try again.")

    
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
