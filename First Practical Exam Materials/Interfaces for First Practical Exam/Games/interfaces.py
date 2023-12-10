from abc import ABC, abstractmethod
from typing import List

class State(ABC):
    """An abstract class defining the State interface."""

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the state.
        Returns:
            str: The string representation of the state.
        """
        pass

class GameState:
    """A class representing a game state."""

    def __init__(self, state: State, player_to_move: object) -> None:
        """Initializes the GameState class.
        Args:
            state (State): The current state.
            player_to_move (object): The player to move.
        """
        self.state = state
        self.player_to_move = player_to_move

    def __str__(self) -> str:
        """Returns the string representation of the game state.
        Returns:
            str: The string representation of the game state.
        """
        return f"{self.state}\nPlayer to move: {self.player_to_move}"


class Action(ABC):
    """An abstract class defining the Action interface."""

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the action.
        Returns:
            str: The string representation of the action.
        """
        pass

class ActionsFunction(ABC):
    """An abstract class defining the Actions Function interface."""

    @abstractmethod
    def actions(self, game_state: GameState) -> List[Action]:
        """Return the actions that can be executed in the given state.
        Args:
            state (GameState): The current state.
        Returns:
            List[Action]: The actions that can be executed in the given state.
        """
        pass

class ResultFunction(ABC):
    """An abstract class defining the Result Function interface."""

    @abstractmethod
    def result(self, game_state: GameState, action: Action) -> GameState:
        """Return the state that results from executing the given action in the given state.
        Args:
            game_state (GameState): The current state.
            action (Action): The action to execute.
        Returns:
            GameState: The state that results from executing the given action in the given state.
        """
        pass
