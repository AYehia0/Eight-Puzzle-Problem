# using deepcopy to have a save of the board as it changes and not assigning it to other var as any change in the board will change the goal
from copy import deepcopy as dc
import os


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
        self.current_empty = {'row':ROWS-1, 'col':COLS-1}

    def __repr__(self):
        """Printing the object of the class prints the board"""

        for row in range(ROWS):
            for col in range(COLS):
                print(self.board[row][col], end=" ")
            print()

        # Returning an empty string is required 
        return ""

    def refresh_screen(self):
        # To clear the screen ,, refresh it 
        os.system('clear')

        # Printing the board
        print(self)

    def move(self, x_pos, y_pos, board, empty_pos):
        """ Templete to handle single movement of an index on the 2D list """

        # Check if a move is valid 
        # Checking if the wanted position is in between the max rows/cols and 0 
        if (empty_pos['row'] + x_pos) < 0 or (empty_pos['row'] + x_pos) > ROWS-1 or (empty_pos['col'] + y_pos) < 0  or (empty_pos['col'] + y_pos) > COLS-1:
            # For now it's return the board and the location of the empty space
            return board, empty_pos

        # Swapping the position of the empty space with the relevent location of the (x_pos, y_pos)
        board[empty_pos['row']][empty_pos['col']], board[empty_pos['row'] + x_pos][empty_pos['col'] + y_pos] = \
        board[empty_pos['row'] + x_pos][empty_pos['col'] + y_pos], board[empty_pos['row']][empty_pos['col']] 

        # updating the position of the empty space
        empty_pos['row'] += x_pos
        empty_pos['col'] += y_pos

        # Returning the board and the empty spot
        return board, empty_pos

    # Move up by decreasing the rows    
    def move_up(self, empty_pos, board):
        return self.move(-1, 0, board, empty_pos)
    
    # Move down by increasing the rows    
    def move_down(self, empty_pos, board):
        return self.move(1, 0, board, empty_pos)

    # Move right by increasing the cols   
    def move_right(self, empty_pos, board):
        return self.move(0, 1, board, empty_pos)

    # Move left by decreasing the cols    
    def move_left(self, empty_pos, board):
        return self.move(0, -1, board, empty_pos)



