from game_algorithms.interfaces import State
from typing import List, Tuple

class XOBoard:
    """This defines the board for the XO game, with some useful methods."""
    def __init__(self, board=None) -> None:
        """Initializes the XOBoard class.
        Args:
            board (List[List[str]], optional): The board. Defaults to None.
        """
        self.num_rows, self.num_columns = 3, 3
        self.board = board if board is not None else self.__create_board()


    def __create_board(self) -> List[List[str]]:
        """Creates the board.
        Returns:
            List[List[str]]: The board.
        """
        return [[" " for _ in range(self.num_rows)] for _ in range(self.num_columns)]
    
    def clone(self) -> "XOBoard":
        """Returns a clone of the board.
        Returns:
            XOBoard: A clone of the board.
        """
        return XOBoard([row[:] for row in self.board])
    
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

    def __check_rows(self, mark: str) -> bool:
        """Checks if the given mark has won in any row.
        Args:
            mark (str): The mark to check (X or O).
        Returns:
            bool: True if the given mark has won in any row, False otherwise.
        """
        for row in self.board:
            if all([value == mark for value in row]):
                return True
        return False
    
    def __check_columns(self, mark: str) -> bool:
        """Checks if the given mark has won in any column.
        Args:
            mark (str): The mark to check (X or O).
        Returns:
            bool: True if the given mark has won in any column, False otherwise.
        """
        for j in range(self.num_columns):
            if all([row[j] == mark for row in self.board]):
                return True
        return False
    
    def __check_diagonals(self, mark: str) -> bool:
        """Checks if the given mark has won in any diagonal.
        Args:
            mark (str): The mark to check (X or O).
        Returns:
            bool: True if the given mark has won in any diagonal, False otherwise.
        """
        if all([self.board[i][i] == mark for i in range(self.num_rows)]):
            return True
        if all([self.board[i][self.num_columns - i - 1] == mark for i in range(self.num_rows)]):
            return True
        return False
    
    def check_win(self, mark: str) -> bool:
        """Checks if the given mark has won.
        Args:
            mark (str): The mark to check (X or O).
        Returns:
            bool: True if the given mark has won, False otherwise.
        """
        return self.__check_rows(mark) or self.__check_columns(mark) or self.__check_diagonals(mark)
    
    def someone_won(self) -> bool:
        """Checks if someone has won.
        Returns:
            bool: True if someone has won, False otherwise.
        """
        return self.check_win("X") or self.check_win("O")
    
    def is_full(self) -> bool:
        """Checks if the board is full.
        Returns:
            bool: True if the board is full, False otherwise.
        """
        return all([value != " " for row in self.board for value in row])

    def is_terminal(self) -> bool:
        """Checks if the board is terminal.
        Returns:
            bool: True if the board is terminal, False otherwise.
        """
        return self.someone_won() or self.is_full()
    
    def __str__(self) -> str:
        """Returns the string representation of the board.
        Returns:
            str: The string representation of the board.
        """
        draw = ""
        for i in range(self.num_rows - 1, -1, -1):
            draw += "|"
            for j in range(self.num_columns):
                draw += self.board[i][j] + "|"
            draw += "\n"
        return draw[:-1]