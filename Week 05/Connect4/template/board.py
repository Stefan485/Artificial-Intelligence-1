from game_algorithms.interfaces import State
from typing import List, Tuple

class Connect4Board(State):
    """This class defines the board of the Connect4 game, with some useful methods."""
    def __init__(self, board_size: Tuple[int, int] = (6, 7), connect: int = 4, board: List[List[str]] = None) -> None:
        """Initializes the Connect4Board class.
        Args:
            board_size (Tuple[int, int], optional): The size of the board (rows, columns). Defaults to (6, 7).
            connect: (int, optional): The number of pieces that must be connected to win. Defaults to 4.
            board (List[List[str]], optional): The board. Defaults to None.
        """
        self.board_size = board_size
        self.connect = connect
        self.board = board if board is not None else self.__create_board()

    def __create_board(self) -> List[List[str]]:
        """Creates the board.
        Returns:
            List[List[str]]: The board.
        """
        return [[" " for _ in range(self.board_size[1])] for _ in range(self.board_size[0])]
    
    def clone(self) -> "Connect4Board":
        """Returns a clone of the board.
        Returns:
            Connect4Board: A clone of the board.
        """
        return Connect4Board(self.board_size, self.connect, [row[:] for row in self.board])
    
    def get_value(self, row: int, column: int) -> str:
        """Returns the value of the given position.
        Args:
            row (int): The row of the position.
            column (int): The column of the position.
        Returns:
            str: The mark at the given position.
        """
        return self.board[row][column]
    
    def set_value(self, row: int, column: int, mark: str) -> None:
        """Sets the value of the given position.
        Args:
            row (int): The row of the position.
            column (int): The column of the position.
            value (str): The mark to set.
        """
        assert mark in ["X", "O"], "The mark must be X or O."
        self.board[row][column] = mark

    def __consecutive_pieces_rows(self, consecutive_pieces: int, mark: str) -> int:
        """Returns the number of times the given mark has consecutive pieces in a row.
        Args:
            consecutive_pieces (int): The number of consecutive pieces that should be in 1 row.
            mark (str): The mark to check (X or O)
        Returns:
            int: Number of times the given mark has consecutive pieces in a row.
        """
        times = 0
        for row in self.board:
            for j in range(len(row) - consecutive_pieces + 1):
                if len(set(row[j:j+consecutive_pieces])) == 1 and row[j] == mark:
                    times += 1
        return times
    
    def __check_rows(self) -> bool:
        """Returns if someone won the game in the rows.
        Returns:
            bool: True if someone won the game in the rows.
        """
        return self.__consecutive_pieces_rows(self.connect, "X") or self.__consecutive_pieces_rows(self.connect, "O")
    
    def __consecutive_pieces_columns(self, consecutive_pieces: int, mark: str) -> int:
        """Returns the number of times the given mark has consecutive pieces in a column.
        Args:
            consecutive_pieces (int): The number of consecutive pieces that should be in 1 column.
            mark (str): The mark to check (X or O)
        Returns:
            int: Number of times the given mark has consecutive pieces in a column.
        """
        times = 0
        for i in range(len(self.board[0])):
            for j in range(len(self.board) - consecutive_pieces + 1):
                if len(set([row[i] for row in self.board[j:j+consecutive_pieces]])) == 1 and self.board[j][i] == mark:
                    times += 1
        return times
    
    def __check_columns(self) -> bool:
        """Returns if someone won the game in the columns.
        Returns:
            bool: True if someone won the game in the columns.
        """
        return self.__consecutive_pieces_columns(self.connect, "X") or self.__consecutive_pieces_columns(self.connect, "O")
    
    def __consecutive_pieces_diagonals(self, consecutive_pieces: int, mark: str) -> int:
        """Returns the number of times the given mark has consecutive pieces in 1 diagonal.
        Args:
            consecutive_pieces (int): The number of consecutive pieces that should be in 1 diagonal.
            mark (str): The mark to check (X or O)
        Returns:
            int: Number of times the given mark has consecutive pieces in 1 diagonal.
        """
        times = 0
        for i in range(len(self.board) - consecutive_pieces + 1):
            for j in range(len(self.board[0]) - consecutive_pieces + 1):
                if len(set([self.board[i+k][j+k] for k in range(consecutive_pieces)])) == 1 and self.board[i][j] == mark:
                    times += 1
        for i in range(len(self.board) - consecutive_pieces + 1):
            for j in range(consecutive_pieces - 1, len(self.board[0])):
                if len(set([self.board[i+k][j-k] for k in range(consecutive_pieces)])) == 1 and self.board[i][j] == mark:
                    times += 1
        return times
    
    def __check_diagonals(self) -> bool:
        """Returns if someone won the game in the diagonals.
        Returns:
            bool: True if someone won the game in the diagonals.
        """
        return self.__consecutive_pieces_diagonals(self.connect, "X") or self.__consecutive_pieces_diagonals(self.connect, "O")
    
    def someone_won(self) -> bool:
        """Returns if someone won the game.
        Returns:
            bool: True if someone won the game.
        """
        return self.__check_rows() or self.__check_columns() or self.__check_diagonals()
    
    def is_full(self) -> bool:
        """Returns if the board is full.
        Returns:
            bool: True if the board is full.
        """
        return all([value != " " for row in self.board for value in row])
    
    def is_terminal(self) -> bool:
        """Returns if the board is terminal.
        Returns:
            bool: True if the board is terminal.
        """
        return self.someone_won() or self.is_full()
    
    def __heuristic_evaluation(self, mark: str) -> float:
        """Returns the heuristic evaluation of the board for the given mark.
        Args:
            mark (str): The mark to check (X or O)
        Returns:
            float: The heuristic evaluation of the board for the given mark.
        """
        score = 0
        for i in range(1, self.connect + 1):
            score += 10 ** i * (self.__consecutive_pieces_rows(i, mark) + 
                                self.__consecutive_pieces_columns(i, mark) + 
                                self.__consecutive_pieces_diagonals(i, mark))
        return score
    
    def heuristic_evaluation(self) -> float:
        """Returns the heuristic evaluation of the board.
        Returns:
            float: The heuristic evaluation of the board.
        """
        return self.__heuristic_evaluation("X") - self.__heuristic_evaluation("O")
    
    def __str__(self) -> str:
        """Returns the string representation of the board.
        Returns:
            str: The string representation of the board.
        """
        draw = ""
        for i in range(self.board_size[0] - 1, -1, -1):
            draw += "|"
            for j in range(self.board_size[1]):
                draw += self.board[i][j] + "|"
            draw += "\n"
        return draw[:-1]
        