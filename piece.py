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
        self._update_top()
        self._update_bottom()
        self._update_left_right()

        self.height = self.top - self.bottom + 1
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

    def move_left(self, bound):
        if self.x <= bound.left:
            return False

        self.x -= 1
        return True

    def move_right(self, bound):
        if self.x + self.width - 1 >= bound.right:
            return False

        self.x += 1
        return True

    def rotate_counter_clockwise(self, bound):
        old_shape = self.shape
        self.shape = zip(*old_shape)[::-1]
        self._update_bound()

        if self.x + self.width - 1 > bound.right:
            self.shape = old_shape
            self._update_bound()
            return False

        return True

    def rotate_clockwise(self, bound):
        old_shape = self.shape
        self.shape = zip(*old_shape[::-1])
        self._update_bound()

        if self.x + self.width - 1 > bound.right:
            self.shape = old_shape
            self._update_bound()
            return False

        return True
