"""This module defines some test examples for the rotationg maze problem."""

from board import RotatingnMazeBoard

tables = [[ [" ", " ", " ", " ", " ", " ", "X"], 
            [" ", " ", " ", " ", " ", "#", " "],
            ["#", "#", " ", " ", " ", " ", "#"],
            ["O", " ", " ", " ", " ", " ", "#"]],

          [ ["O", " ", " "],
            ["#", "#", " "],
            ["X", " ", " "]],

          [ ["O", " ", " ", " "],
            ["#", "#", " ", " "],
            [" ", " ", " ", "#"],
            ["X", "#", "#", "#"]],
        
          [ [" ", " ", " ", "O", " ", " ", " ", " "], 
            [" ", " ", "#", "#", "#", " ", " ", " "],
            [" ", " ", " ", " ", " ", "#", " ", " "],
            ["#", " ", " ", "#", "#", "#", " ", "#"],
            [" ", " ", " ", " ", " ", "#", " ", " "],
            [" ", " ", " ", "#", " ", " ", " ", "X"]],
        
          [ ["O", " ", " "], 
            ["#", "#", " "],
            [" ", " ", " "],
            [" ", "#", "#"],
            [" ", " ", " "],
            ["#", "#", " "], 
            ["X", " ", " "],
            [" ", " ", " "]],
        
          [ ["O", " ", " ", " ", "#", " ", " ", " "],
            ["#", "#", "#", " ", "#", " ", "#", " "],
            [" ", " ", " ", " ", "#", " ", "#", " "],
            ["#", " ", " ", " ", " ", " ", "#", " "],
            ["#", " ", "#", "#", "#", "#", "#", " "],
            ["#", " ", " ", " ", "#", " ", " ", " "],
            ["#", " ", " ", " ", " ", " ", "#", "#"],
            ["#", " ", " ", "#", " ", " ", " ", "X"]],

          [ ["O", " ", " ", " "],
            ["#", "#", " ", " "],
            [" ", " ", " ", " "],
            ["X", "#", "#", " "]],
        
          [ ["X", "#", "#", "#"],
            ["#", " ", "#", "#"],
            ["#", " ", " ", "#"],
            [" ", " ", " ", "#"],
            [" ", " ", " ", " "],
            ["#", "#", " ", "O"]]

        ]

# use this list of boards to test your code
boards = [RotatingnMazeBoard(table, len(table), len(table[0])) for table in tables]
