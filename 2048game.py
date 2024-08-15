import random

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.board[i][j] = random.choice([2, 4])

    def compress(self, row):
        new_row = [i for i in row if i != 0]
        new_row += [0] * (4 - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]
        return row

    def move_left(self):
        new_board = []
        for row in self.board:
            compressed_row = self.compress(row)
            merged_row = self.merge(compressed_row)
            new_row = self.compress(merged_row)
            new_board.append(new_row)
        self.board = new_board

    def rotate_board_clockwise(self):
        self.board = [list(row) for row in zip(*self.board[::-1])]

    def move_right(self):
        self.rotate_board_clockwise()
        self.rotate_board_clockwise()
        self.move_left()
        self.rotate_board_clockwise()
        self.rotate_board_clockwise()

    def move_up(self):
        self.rotate_board_clockwise()
        self.rotate_board_clockwise()
        self.rotate_board_clockwise()
        self.move_left()
        self.rotate_board_clockwise()

    def move_down(self):
        self.rotate_board_clockwise()
        self.move_left()
        self.rotate_board_clockwise()
        self.rotate_board_clockwise()
        self.rotate_board_clockwise()

    def is_game_over(self):
        for row in self.board:
            if 0 in row:
                return False
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j + 1] or self.board[j][i] == self.board[j + 1][i]:
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(row)
        print(f"Score: {self.score}")

# Example usage:
game = Game2048()
game.print_board()
game.move_left()
game.print_board()
game.move_up()
game.print_board()