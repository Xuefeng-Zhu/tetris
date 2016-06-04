import random

from config import HEIGHT, WIDTH


SHAPE_SIZE = 4


def create_piece_shape(shape):
    result = [[False] * SHAPE_SIZE for _ in range(SHAPE_SIZE)]
    for pos in shape:
        y = pos / SHAPE_SIZE
        x = pos % SHAPE_SIZE
        result[y][x] = True

    return result


class Piece:
    A = create_piece_shape([0, 1, 2, 3])
    B = create_piece_shape([0, 4, 8, 9])
    C = create_piece_shape([1, 5, 8, 9])
    D = create_piece_shape([1, 4, 5, 8])
    E = create_piece_shape([0, 1, 4, 5])

    TYPES = [A, B, C, D, E]

    def __init__(self):
        type_index = random.randint(0, len(self.TYPES) - 1)
        self.shape = self.TYPES[type_index]
        self._update_bound()

        self.y = self.height - 1
        self.x = random.randint(0, WIDTH - self.width)

    def _update_bound(self):
        '''
            Get bound information for the piece
        '''
        self._update_top()
        self._update_bottom()
        self._update_left_right()

        self.height = self.bottom - self.top + 1
        self.width = self.right - self.left + 1

    def _update_top(self):
        for index, row in enumerate(self.shape):
            if True in row:
                self.top = index
                return

    def _update_bottom(self):
        for index, row in enumerate(self.shape):
            if True in row:
                self.bottom = index

    def _update_left_right(self):
        left = None
        right = None
        for row in self.shape:
            count = row.count(True)
            if count > 0:
                l_index = row.index(True)
                r_index = l_index + count - 1
                if left is None or l_index < left:
                    left = l_index

                if right is None or r_index > right:
                    right = r_index

        self.left = left
        self.right = right

    def move(self, action):
        '''
            Dispatch the action to specifc movement
        '''
        self.old_x = self.x
        self.old_shape = self.shape
        self.y += 1
        getattr(self, action)()
        self._update_bound()

    def undo(self):
        '''
            Undo previous movement
        '''
        self.x = self.old_x
        self.shape = self.old_shape
        self.y -= 1
        self._update_bound()

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        pass

    def rotate_counter_clockwise(self):
        self.shape = zip(*self.shape)[::-1]

    def rotate_clockwise(self):
        self.shape = zip(*self.shape[::-1])
