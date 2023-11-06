import math
from search_algorithms.interfaces import State, Action, ActionsFunction, ResultFunction, GoalTestFunction, StepCostFunction, HeuristicFunction

class WordState(State):
    def __init__(self, word):
        self.word = word

    def __str__(self) -> str:
        return self.word

    def __eq__(self, other: object) -> bool:
        if self.word is None or other.word is None:
            return False
        if not isinstance(other, WordState):
            return False
        if self.word == other.word:
            return False
        return True
    
    def __hash__(self) -> int:
        return hash(self.word)
    
class WordAction(Action):
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self) -> str:
        return f"Swap positions {self.i} and {self.j}"
    
class WordActionsFunction(ActionsFunction):
    def actions(self, state: State):
        return [WordAction(i, j) for i in range(len(state.word)) for j in range(i + 1, len(state.word))]
    
class WordResultFunction(ResultFunction):
    def result(self, state: State, action: Action):
        i, j = action.i, action.j
        word =  state.word[:i] + state.word[j] + state.word[i+1:j] + state.word[i] + state.word[j+1:]
        return WordState(word)
    
class WordGoalTestFunction(GoalTestFunction):
    def __init__(self, goal_word):
        self.goal_word = goal_word

    def is_goal_state(self, state: State) -> bool:
        return state.word == self.goal_word
    
class WordStepCostFunction(StepCostFunction):
    def cost(self, state: State, action: Action, state1: State) -> float:
        return 1
    
class WordHeuristicFunction(HeuristicFunction):
    def __init__(self, goal_word):
        self.goal_word = goal_word

    def h(self, state: State) -> float:
        assert len(state.word) == len(self.goal_word), "Words needs to be of the same length"
        sum = 0
        for i in range(len(state.word)):
            if state.word[i] != self.goal_word[i]:
                sum += 1
        return math.ceil(sum / 2)
