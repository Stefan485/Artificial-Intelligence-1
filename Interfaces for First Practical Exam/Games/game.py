from abc import ABC, abstractmethod

from .interfaces import GameState,  Action, ActionsFunction, ResultFunction

class Game(ABC):

    def __init__(self, actions_function: ActionsFunction, result_function: ResultFunction,
                 max_player: bool = True) -> None:
        """Initializes the Game class.
        Args:
            actions_function (ActionsFunction): The actions function.
            result_function (ResultFunction): The result function.
            max_player (bool): Whether minimax agent is maximizing or minimizing player. Defaults to True.
        """
        self.actions_function = actions_function
        self.result_function = result_function
        self.max_player = max_player

    @abstractmethod
    def is_terminal(self, game_state: GameState) -> bool:
        """Returns if the given state is terminal.
        Args:
            state (GameState): The current game state.
        Returns:
            bool: True if the given state is terminal.
        """
        pass

    @abstractmethod
    def compute_utility(self, game_state: GameState) -> float:
        """Returns the utility of the given state. This method can be called if the state
            is terminal (and then it returns the score for the winner) or if the state is 
            non-terminal (and then it returns the heuristic evaluation of the state).
        Args:
            state (GameState): The current game state.
        Returns:
            float: The utility of the given state.
        """
        pass