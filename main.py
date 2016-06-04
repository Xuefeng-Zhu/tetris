from __future__ import print_function

from manager import Manager
from config import ACTIONS


def show_instruction():
    print('TETRIS CLI')
    print('AVAILABLE ACTIONS')
    for key, action in ACTIONS.items():
        print('{}: {}'.format(key, action.replace('_', ' ')))
    print('---------------------------')

if __name__ == '__main__':
    show_instruction()
    manager = Manager()
    while True:
        manager.game_loop()
