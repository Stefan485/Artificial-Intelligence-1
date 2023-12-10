from typing import List

class RotatingnMazeBoard:
    
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
        return isinstance(other, RotatingnMazeBoard) and self.board == other.board and self.num_rows == other.num_rows and self.num_columns == other.num_columns
    
    def __hash__(self) -> int:
        """Returns the hash value of this object.
        
        Returns:
            int: The hash value of this object.
        """
        return hash(str(self.board))
    
    def __str__(self) -> str:
        """Returns the string representation of the board.
        
        Returns:
            str: The string representation of the board.
        """
        result = "-" * (2 * self.num_columns + 1) + "\n"
        for row in self.board:
            result += "|"
            result += " ".join([cell for cell in row]) + "|\n"
        result += "-" * (2 * self.num_columns + 1)
        return result
    
    def clone(self) -> "RotatingnMazeBoard":
        """Returns a clone object of the board.
        
        Returns:
            EightPuzzleBoard: A clone of the board.
        """
        return RotatingnMazeBoard([row[:] for row in self.board], self.num_rows, self.num_columns)
    
    def get_value(self, row: int, column: int) -> int:
        """Returns the value at the given position on the board.
        
        Args:
            row (int): The row.
            column (int): The column.
            
        Returns:
            int: The value at the given position on the board.
        """
        return self.board[row][column]
    
    def set_value(self, row: int, column: int, value: int) -> None:
        """Sets the value at the given position on the board.
        
        Args:
            row (int): The row.
            column (int): The column.
            value (int): The value.
        """
        self.board[row][column] = value
    
    def get_goal_position(self) -> (int, int):
        """Returns the position of the goal cell on a board.
        
        Returns:
            (int, int): The position of the goal cell (row, column).
        """
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self.board[i][j] == "X":
                    return i, j
        return None
    
    def get_ball_position(self) -> (int, int):
        """Returns the position of the ball cell on a board.
        
        Returns:
            (int, int): The position of the ball cell (row, column).
        """
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if self.board[i][j] == "O":
                    return i, j
        return None


   