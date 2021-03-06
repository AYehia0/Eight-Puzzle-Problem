# using deepcopy to have a save of the board as it changes and not assigning it to other var as any change in the board will change the goal
from copy import deepcopy as dc
import random
from queue import Queue
import os


ROWS = 3
COLS = 3
RANDOM_SUFFLE = 200

class Board:
    """To handle board spacific things"""
    def __init__(self):
        self.goal = [['1','2','3'],
                     ['4','5','6'],
                     ['7','8','_']]
        self.board = dc(self.goal)
        # To keep track of the empty space aka '_'
        self.current_empty = {'row':ROWS-1, 'col':COLS-1}
        self.winner = False
        self.valid_moves = {0: self.move_up, 1: self.move_down, 2:self.move_right, 3:self.move_left}

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

        # Checking if game over
        if self.won():
            return False

        return True


    def randomize_board(self):
        """ Randomize the board by moving places """
        random.seed()
        for _ in range(RANDOM_SUFFLE):
            r = random.randint(0,3)
            self.valid_moves[r](self.current_empty, self.board)

        # Swaps the postion of the '_' empty space to (2,2), 2 ways
        for _ in range(ROWS):
            self.valid_moves[2](self.current_empty, self.board)

        for _ in range(COLS):
            self.valid_moves[1](self.current_empty, self.board)

    def won(self):
        """ Check if board is solved """

        if self.board == self.goal:
            print('/nYou Won!!')
            self.winner =True
            return True

        return False

    def quick_solve(self):
        """ solves the game by copying the goal to board """
        self.board = dc(self.goal)

    def solve_game(self):
        """ BFS implementation for solving the board """

        # Helper function to get the node childrens
        def node_childrens(board , empty_pos):

            # List of all Operators for both board (up,down,right,left) and empty spot
            boards_op = [dc(board) for _ in range(4)]
            empty_spots_op = [dict(empty_pos) for _ in range(4)]

            
            # moves
            boards_op[0], empty_spots_op[0] =  self.move_up(empty_spots_op[0], boards_op[0])  # UP
            boards_op[1], empty_spots_op[1] =  self.move_down(empty_spots_op[1], boards_op[1]) # DOWN
            boards_op[2], empty_spots_op[2] =  self.move_right(empty_spots_op[2], boards_op[2]) # RIGHT
            boards_op[3], empty_spots_op[3] =  self.move_left(empty_spots_op[3], boards_op[3]) # LEFT
            

            # location of up, empty_up, INT: which way we moved
            return [[boards_op[0], empty_spots_op[0], 0], [boards_op[1], empty_spots_op[1], 1], [boards_op[2], empty_spots_op[2], 2], [boards_op[3], empty_spots_op[3], 3]]



        # to add visited nodes in 
        visited = []

        # making a queue to keep track of children nodes 
        queue = []
        queue.append({'board':self.board, 'empty_pos':self.current_empty, 'path':[]})

        while True:

            # print(queue.get())
            if len(queue)==0:
                return []

            # popping the first in the queue
            node = queue.pop(0)

            # Quit if goal is found
            if node['board'] == self.goal:
                # Returning the path 
                return node['path']

            if node['board'] not in visited:
                # mark the board as visited
                visited.append(node['board'])

                # get its childrens 
                for child in node_childrens(node['board'], node['empty_pos']):
                    # the board 
                    if child[0] not in visited:
                        queue.append({'board':child[0], 'empty_pos':child[1], 'path':node['path'] + [child[2]] })


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



