from __future__ import print_function

from display import Display
from piece import Piece
from config import ACTIONS, OverlapError


class Manager:

    def __init__(self):
        self.display = Display()
        self._spawn_piece()

    def _spawn_piece(self):
        '''
            Produce a new piece
        '''
        self.display.update_board()
        self.current_piece = Piece()
        try:
            self.display.add_piece(self.current_piece)
            self.display.draw()
        except OverlapError:
            print('Game Over')
            exit()

    def game_loop(self):
        '''
            Execute for each user input
        '''
        move = raw_input('Please enter a move: ').strip()
        action = ACTIONS.get(move)

        if action is None:
            print('Entered move does not exist! Try again.')
            return

        self.current_piece.move(action)
        try:
            self.display.show_piece()
        except OverlapError:
            self.current_piece.undo()
            print('Invalid move! Try again.')
            return

        if self.display.check_valid_moves():
            self.display.draw()
        else:
            self._spawn_piece()
