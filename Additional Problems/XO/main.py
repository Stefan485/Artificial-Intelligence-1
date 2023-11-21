from board import XOBoard
from game_definition import XOState, XOAction, XOActionsFunction, XOResultFunction, XOGame
from game_algorithms.interfaces import *
from game_algorithms.game import Game
from agent import Agent, Human, AI

def play(game: Game, initial_state: XOState, agent1: Agent, agent2: Agent):
    """Plays the game.
    Args:
        game (Game): The game.
        initial_state (Connect4State): The initial state.
        agent1 (Agent): The first agent.
        agent2 (Agent): The second agent.
    """
    current_state = initial_state
    while not game.is_terminal(current_state):
        print(current_state)
        action = None
        if current_state.player_to_move == agent1.mark:
            action = agent1.make_move(current_state)
        else:
            action = agent2.make_move(current_state)
        current_state = game.result_function.result(current_state, action)
    print(current_state)
    if current_state.state.check_win("X"):
        print(f"The winner is {agent1}!")
    elif current_state.state.check_win("O"):
        print(f"The winner is {agent2}!")
    else:
        print("It's a tie")

if __name__ == "__main__":
    board = XOBoard()
    initial_state = XOState(board, "X")
    actions_function = XOActionsFunction()
    result_function = XOResultFunction()
    game = XOGame(actions_function, result_function, max_player=True, alpha_beta_prunning=True)

    agent1 = AI(game, "X", "AI")
    agent2 = Human(game, "O", "Human")

    play(game, initial_state, agent1, agent2)