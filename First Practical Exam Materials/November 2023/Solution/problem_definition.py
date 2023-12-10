from typing import List

from search_algorithms.interfaces import State, Action, ActionsFunction, ResultFunction, GoalTestFunction, StepCostFunction
from board import RotatingnMazeBoard

class RotatingMazeState(State):
    def __init__(self, board: RotatingnMazeBoard) -> None:
        """Initializes the state.
        
        Args:
            board (RotatingnMazeBoard): The board.
        """
        self.board = board

    def __eq__(self, other: object) -> bool:
        """Checks if the given object is equal to this object.
        
        Args:
            other (object): The other object.
        """
        return isinstance(other, RotatingMazeState) and self.board == other.board
    
    def __hash__(self) -> int:
        """Returns the hash value of this object.
        
        Returns:
            int: The hash value of this object.
        """
        return hash(self.board)
    
    def __str__(self) -> str:
        """Returns the string representation of the state.
        
        Returns:
            str: The string representation of the state.
        """
        return str(self.board)
    
class RotatingMazeAction(Action):
    def __init__(self, clockwise: bool) -> None:
        """Initializes the action.
        
        Args:
            row (int): The row.
            column (int): The column.
        """
        self.clockwise = clockwise
    
    def __str__(self) -> str:
        """Returns the string representation of the action.
        
        Returns:
            str: The string representation of the action.
        """
        return "Clockwise" if self.clockwise else "Counter-clockwise"
    
class RotatingMazeActionsFunction(ActionsFunction):
    def actions(self, state: RotatingMazeState) -> List[RotatingMazeAction]:
        """Returns the list of actions that can be executed in the given state.
        
        Args:
            state (RotatingMazeState): The state.
            
        Returns:
            List[RotatingMazeAction]: The list of actions that can be executed in the given state.
        """
        return [RotatingMazeAction(True), RotatingMazeAction(False)]
    
class RotatingMazeResultFunction(ResultFunction):
    def result(self, state: RotatingMazeState, action: RotatingMazeAction) -> RotatingMazeState:
        """Returns the state that results from executing the given action in the given state.
        
        Args:
            state (RotatingMazeState): The state.
            action (RotatingMazeAction): The action.
            
        Returns:
            RotatingMazeState: The state that results from executing the given action in the given state.
        """
        new_board = state.board.rotate(action.clockwise)
        new_board.drop_ball()
        return RotatingMazeState(new_board)
    
class RotatingMazeGoalTestFunction(GoalTestFunction):
    def is_goal_state(self, state: RotatingMazeState) -> bool:
        """Checks if the given state is a goal state.
        
        Args:
            state (RotatingMazeState): The state.
            
        Returns:
            bool: True if the given state is a goal state, False otherwise.
        """
        return state.board.get_ball_position() is None
    
class RotatingMazeStepCostFunction(StepCostFunction):
    def cost(self, state: RotatingMazeState, action: RotatingMazeAction) -> float:
        """Returns the cost of taking the given action in the given state.
        
        Args:
            state (RotatingMazeState): The state.
            action (RotatingMazeAction): The action.
            
        Returns:
            float: The cost of taking the given action in the given state.
        """
        return 1.0
