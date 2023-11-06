from typing import List
from search_algorithms.interfaces import State, Action, ActionsFunction, ResultFunction, GoalTestFunction, StepCostFunction, HeuristicFunction

class RomanianMapState(State):
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        return isinstance(other, RomanianMapState) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)
    
    
class RomanianMapAction(Action):
    def __init__(self, to_city):
        self.to_city = to_city

    def __str__(self) -> str:
        return f"Go to {self.to_city}"
    
    
class RomanianMapActionsFunction(ActionsFunction):
        def __init__(self, city_connections):
           self.city_connections = city_connections

        def actions(self, state: State) -> List[Action]:
            assert isinstance(state, RomanianMapState)
            actions = []
            for (city1, city2, _) in self.city_connections:
                if city1 == state.name:
                    actions.append(RomanianMapAction(city2))
                elif city2 == state.name:
                    actions.append(RomanianMapAction(city1))
            return actions
        

class RomanianMapResultFunction(ResultFunction):

    def result(self, state: object, action: object) -> object:
        assert isinstance(action, RomanianMapAction)
        return RomanianMapState(action.to_city)
    
class RomanianMapGoalTestFunction(GoalTestFunction):
    def is_goal_state(self, state):
        assert isinstance(state, State)
        return state.name == "Bucharest"
    
class RomanianMapStepCostFunction(StepCostFunction):
    def __init__(self, city_connections):
        self.city_connections = city_connections

    def cost(self, state: State, action: Action, state1: State) -> float:
        assert isinstance(state, RomanianMapState)
        assert isinstance(action, RomanianMapAction)
        assert isinstance(state1, RomanianMapState)
        for (city1, city2, cost) in self.city_connections:
            if (city1 == state.name and city2 == state1.name) or (city2 == state.name and city1 == state1.name):
                return cost
        raise Exception(f"Invalid state transition: {state} to {state1}")
    
class RomanianMapHeuristicFunction(HeuristicFunction):
    def __init__(self, straight_line_distances):
        self.straight_line_distances = straight_line_distances

    def h(self, state: State) -> float:
        return self.straight_line_distances[state.name]