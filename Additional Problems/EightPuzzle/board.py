from typing import List, Dict, Tuple

class EightPuzzleBoard:

    def __init__(self, board: List[List[int]], num_rows: int, num_columns: int) -> None:
        """Initializes the board.
        
        Args:
            board (List[List[int]]): The board.
            num_rows (int): The number of rows.
            num_columns (int): The number of columns.
        """
        self.board = board
        self.num_rows = num_rows
        self.num_columns = num_columns

    def __eq__(self, other: object) -> bool:
        """Checks if the given object is equal to this object.
        
        Args:
            other (object): The other object.
        """
        return isinstance(other, EightPuzzleBoard) and self.board == other.board and self.num_rows == other.num_rows and self.num_columns == other.num_columns

    def __str__(self) -> str:
        """Returns the string representation of the board.
        
        Returns:
            str: The string representation of the board.
        """
        return '\n'.join([' '.join([str(cell) if cell != 0 else ' ' for cell in row]) for row in self.board])
    
    def clone(self) -> "EightPuzzleBoard":
        """Returns a clone object of the board.
        
        Returns:
            EightPuzzleBoard: A clone of the board.
        """
        return EightPuzzleBoard([row[:] for row in self.board], self.num_rows, self.num_columns)

    def get_blank_position(self) -> (int, int):
        """Returns the position of the blank cell on a board.
        
        Returns:
            (int, int): The position of the blank cell (row, column).
        """
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self.board[i][j] == 0:
                    return i, j
        return None
    
    def get_board_dimensions(self) -> (int, int):
        """Returns the dimensions of the board.
        
        Returns:
            (int, int): The dimensions of the board (num_rows, num_columns).
        """
        return self.num_rows, self.num_columns
    
    def get_value(self, row: int, column: int) -> int:
        """Returns the value of the given position.
        
        Args:
            row (int): The row of the position.
            column (int): The column of the position.
            
        Returns:
            int: The value of the given position.
        """
        return self.board[row][column]
    
    def set_value(self, row: int, column: int, value: int) -> None:
        """Sets the value of the given position.
        
        Args:
            row (int): The row of the position.
            column (int): The column of the position.
            value (int): The value to set.
        """
        assert value in range(self.num_rows * self.num_columns), \
                f"The value must be between 0 and {self.num_rows * self.num_columns - 1}."
        self.board[row][column] = value

    def get_positions_for_each_tile(self) -> Dict[int, Tuple[int, int]]:
        """Returns a dictionary with the positions of each tile in the order of value of the tile.
        
        Returns:
            dict: A dictionary with the positions of each tile.
        """
        positions = {}
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                positions[self.board[i][j]] = (i, j)
        return positions
    
    @staticmethod
    def create_goal_board(num_rows: int, num_columns: int) -> "EightPuzzleBoard":
        board = [[i * num_columns + j for j in range(num_columns)] for i in range(num_rows)]
        return EightPuzzleBoard(board, num_rows, num_columns)

    

