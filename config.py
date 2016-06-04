HEIGHT = 20
WIDTH = 20

ACTIONS = {
    'a': 'move_left',
    'd': 'move_right',
    'n': 'move_down',
    'w': 'rotate_counter_clockwise',
    's': 'rotate_clockwise',
}


class OverlapError(Exception):
    pass
