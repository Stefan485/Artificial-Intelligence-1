from board import Connect4Board
from game_definition import Connect4State, Connect4Action, Connect4ActionsFunction, Connect4ResultFunction, Connect4Game
from game_algorithms.interfaces import *
from game_algorithms.game import Game
from agent import Agent, Human, AI

def play(game: Game, initial_state: Connect4State, agent1: Agent, agent2: Agent):
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
    if current_state.state.someone_won():
        winner = agent1 if current_state.player_to_move == agent2.mark else agent2
        print(f"The winner is {winner}!")
    else:
        print("It's a tie")

if __name__ == "__main__":
    board = Connect4Board(board_size=(6, 7), connect=4)
    initial_state = Connect4State(board, "X")
    actions_function = Connect4ActionsFunction()
    result_function = Connect4ResultFunction()
    game = Connect4Game(actions_function, result_function, max_player=True, alpha_beta_prunning=True, max_depth=5)

    agent1 = AI(game, "X", "AI")
    agent2 = Human(game, "O", "Human")

    play(game, initial_state, agent1, agent2)