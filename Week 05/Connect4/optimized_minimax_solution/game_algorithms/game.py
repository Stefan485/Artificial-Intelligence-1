from abc import ABC, abstractmethod

from .interfaces import GameState,  Action, ActionsFunction, ResultFunction

class Game(ABC):

    def __init__(self, actions_function: ActionsFunction, result_function: ResultFunction,
                 max_player: bool = True, alpha_beta_prunning: bool = False, max_depth: int = None) -> None:
        """Initializes the Game class.
        Args:
            actions_function (ActionsFunction): The actions function.
            result_function (ResultFunction): The result function.
            max_player (bool): Whether minimax agent is maximizing or minimizing player. Defaults to True.
            alpha_beta_prunning (bool, optional): If alpha-beta prunning should be used. Defaults to False.
            max_depth (int, optional): The maximum depth. Defaults to 10.
        """
        self.actions_function = actions_function
        self.result_function = result_function
        self.max_player = max_player
        self.max_depth = max_depth
        self.alpha_beta_prunning = alpha_beta_prunning

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

    def minimax_decision(self, state: GameState) -> Action:
        """Returns the action that the current player should take.
        Args:
            state (GameState): The current game state.
        Returns:
            Action: The action that the current player should take.
        """
        # Initialize the best action and value.
        best_action = None
        best_value = float("-inf")
        alpha = float("-inf") if self.alpha_beta_prunning else None
        beta = float("inf") if self.alpha_beta_prunning else None
        depth = 0
        # Loop through the actions of the state
        print("Looping through actions")
        for action in self.actions_function.actions(state):
            # Compute the value of the action.
            value = self.__min_value(self.result_function.result(state, action), alpha, beta, depth)
            # Update the best action and value.
            if value > best_value:
                best_action = action
                best_value = value

        return best_action
        
    
    def __max_value(self, state: GameState, alpha: float = None, beta: float = None, depth: int = 0) -> float:
        """Returns the maximum value of the given state in minimax algorithm.
        Args:
            state (GameState): The current game state.
            alpha (float): The alpha value (for prunning).
            beta (float): The beta value (for prunning).
            depth (int): Current depth in minimax tree.
        Returns:
            float: The maximum value of the given state in minimax algorithm.
        """
        if self.alpha_beta_prunning:
            assert alpha is not None and beta is not None, "Alpha and beta values must be provided."
        # If the state is terminal, return the utility of the state.
        if self.is_terminal(state) or (self.max_depth is not None and depth >= self.max_depth):
            return self.compute_utility(state) if self.max_player else -self.compute_utility(state)
        # Initialize the maximum value.
        v = float("-inf")
        # Loop through the actions of the state.
        for action in self.actions_function.actions(state):
            v = max(v, self.__min_value(self.result_function.result(state, action), alpha, beta, 
                                        depth + 1 if self.max_depth is not None else depth))
            # Alpha-beta prunning
            if self.alpha_beta_prunning:
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
        return v
    
    def __min_value(self, state: GameState, alpha: float = None, beta: float = None, depth: int = None) -> float:
        """Returns the minimum value of the given state in minimax algorithm.
        Args:
            state (GameState): The current game state.
            alpha (float): The alpha value (for prunning).
            beta (float): The beta value (for prunning).
            depth (int): Current depth in minimax tree.
        Returns:
                float: The minimum value of the given state in minimax algorithm.
        """
        if self.alpha_beta_prunning:
            assert alpha is not None and beta is not None, "Alpha and beta values must be provided."
        # If the state is terminal, return the utility of the state.
        if self.is_terminal(state) or (self.max_depth is not None and depth >= self.max_depth):
            return self.compute_utility(state) if self.max_player else -self.compute_utility(state)
        # Initialize the minimum value.
        v = float("inf")
        # Loop through the actions of the state.
        for action in self.actions_function.actions(state):
            v = min(v, self.__max_value(self.result_function.result(state, action), alpha, beta, 
                                        depth + 1 if self.max_depth is not None else depth))
            # Alpha-beta prunning
            if self.alpha_beta_prunning:
                beta = min(beta, v)
                if beta <= alpha:
                    break
        return v
