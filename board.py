# using deepcopy to have a save of the board as it changes and not assigning it to other var as any change in the board will change the goal
from copy import deepcopy as dc


ROWS = 3
COLS = 3

class Board:
    """To handle board spacific things"""
    def __init__(self):
        self.goal = [['1','2','3'],
                     ['4','5','6'],
                     ['7','8','_']]
        self.board = dc(self.goal)
        # To keep track of the empty space aka '_'
        self.current_empty = (ROWS-1, COLS-1)

    def __repr__(self):
        """Printing the object of the class prints the board"""

        for row in range(ROWS):
            for col in range(COLS):
                print(self.board[row][col], end=" ")
            print()

        # Returning an empty string is required 
        return ""
