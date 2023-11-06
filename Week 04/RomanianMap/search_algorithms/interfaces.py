from abc import ABC, abstractmethod
from typing import List

class State(ABC):
    """An abstract class defining the State interface."""

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Returns if other object is equal to this object.
        Args:
            other (object): The other object.
        Returns:
            bool: True if other obejct is equal to this object.
        """
        pass

    @abstractmethod
    def __hash__(self) -> int:
        """Returns the hash of this object.
        Returns:
            int: The hash of this object.
        """
        pass

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
    def actions(self, state: State) -> List[Action]:
        """Return the actions that can be executed in the given state.
        Args:
            state (State): The current state.
        Returns:
            List[Action]: The actions that can be executed in the given state.
        """
        pass

class ResultFunction(ABC):
    """An abstract class defining the Result Function interface."""

    @abstractmethod
    def result(self, state: State, action: Action) -> State:
        """Return the state that results from executing the given action in the given state.
        Args:
            state (State): The current state.
            action (Action): The action to execute.
        Returns:
            State: The state that results from executing the given action in the given state.
        """
        pass

class GoalTestFunction(ABC):
    """An abstract class defining the Goal Test interface."""

    @abstractmethod
    def is_goal_state(self, state: State) -> bool:
        """Return True if the state is a goal.
        Args:
            state (State): The current state.
        Returns:
            bool: True if the state is a goal.
        """
        pass

class StepCostFunction(ABC):
    """An abstract class defining the Step Cost Function interface."""

    @abstractmethod
    def cost(self, state: State, action: Action, state1: State) -> float:
        """Return the cost of taking action in state to reach state1.
        Args:
            state (State): The current state.
            action (Action): The action to execute.
            state1 (State): The next state.
        Returns:
            float: The cost of taking action in state to reach state1.
        """
        pass


class HeuristicFunction(ABC):
    """An abstract class defining the Heuristic Function interface."""

    @abstractmethod
    def h(self, state: State) -> float:
        """Return the heuristic estimate of cost to reach a goal state from the given state.
        Args:
            state (State): The current state.
        Returns:
            float: The heuristic estimate of cost to reach a goal state from the given state.
        """
        pass