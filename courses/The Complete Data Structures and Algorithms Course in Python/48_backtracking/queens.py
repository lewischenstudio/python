"""N Queens Problem"""


class NQueens:
    """
    size: the size of the matrix
    queens: number of queens to be placed in the matrix
    """

    def __init__(self, size, queens) -> None:
        self.size = size
        self.queens = queens
        self.chess_table = [[0 for i in range(size)] for j in range(size)]

    def print_queens(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print("\n")

    def is_place_safe(self, row_index, col_index):
        """Checks whether the next queen can be placed in this cell"""
        # checks horizontally
        for i in range(self.size):
            if self.chess_table[row_index][i] == 1:
                return False
        # top left to right bottom (left diagonal \)
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
        # top right to bottom left (right diagonal /)
        j = col_index
        for i in range(row_index, self.size):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
        return True

    def solve(self, col_index):
        """The main method to solve the problem"""
        # 0, 1, 2, 3 --> 4 --> True
        if col_index == self.queens:
            return True

        # increase row index for the next queen to move down
        for row_index in range(self.size):
            if self.is_place_safe(row_index, col_index):
                # if this place is safe, update the cell to 1
                self.chess_table[row_index][col_index] = 1

                # place successive queens without any issue
                if self.solve(col_index + 1):
                    return True

                # backtracking: initialize the current cell to 0
                # after we considered all rows in a given column
                # without finding a valid cell for the queen
                self.chess_table[row_index][col_index] = 0

        return False

    def solve_queen(self):
        """Final method to run the algorithm from the first queen"""
        if self.solve(0):
            self.print_queens()
        else:
            print(
                f"There is no solution for the problem with {self.size}x"
                + f"{self.size} Queens Problem"
            )


queens = NQueens(4, 2)
queens.solve_queen()
