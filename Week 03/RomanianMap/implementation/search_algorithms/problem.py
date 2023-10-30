from .interfaces import State, ActionsFunction, ResultFunction, GoalTestFunction, StepCostFunction

class Problem:
    """This class defines search problem"""

    def __init__(self, initial_state: State, 
                 actions_function: ActionsFunction, 
                 result_function: ResultFunction, 
                 goal_test: GoalTestFunction, 
                 step_cost_function: object):
        """Initialize the problem.
        Args:
            initial_state (object): The initial state.
            actions_function (object): The actions function.
            result_function (object): The result function.
            goal_test (object): The goal test.
            step_cost_function (object): The step cost function.
        """
        assert initial_state is not None, "The initial state cannot be None"
        assert isinstance(initial_state, State), "The initial state must be an instance of State"
        assert isinstance(actions_function, ActionsFunction), "The actions function must be an instance of ActionsFunction"
        assert isinstance(result_function, ResultFunction), "The result function must be an instance of ResultFunction"
        assert isinstance(goal_test, GoalTestFunction), "The goal test must be an instance of GoalTest"
        assert isinstance(step_cost_function, StepCostFunction), "The step cost function must be an instance of StepCostFunction"

        self.initial_state = initial_state
        self.actions_function = actions_function
        self.result_function = result_function
        self.goal_test = goal_test
        self.step_cost_function = step_cost_function