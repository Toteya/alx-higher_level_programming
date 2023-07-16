""" Module 101-nqueens
Solves the N-Queens problem:
Places N non-attaccking queens on an N x N chessboard
"""
import sys
class Queen:
    """ A queen chesspiece """
	
    def __init__(self, position=None):
        self.position = position

    @property
    def position(self):
        """ The position of the chess piece on the chess board """
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) and position != None:
            raise TypeError("position must be a tuple in the form of (x, y)")
        if len(position) != 2:
            raise ValueError("position value must be in the form of (x, y)")
        self.__position = position

def solve_nqueen(N):
    """ Solves the n-queens problem

    Args:
        N (int): Number of queens, and the size of the chessboard
    """
    queens = []
    for i in range(N):
        queens.append(Queen(i, 0))

    solutions = []
    queen_positions = []
    added = False

    for i in range(N):
        queen[i].position[1] = [i]
        for j in range

    for queen in queens:
        for i in range(N):
            if any(q.position[0] == i for q in queens)
            continue
            for j in range(N):
                if any(q.position[1] == j for q in queens)
                continue
                queen.position = (i, j)
                queen_positions.append(queen.position)




if __name__ = "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    if notisinstance(N, int) or N < 4:
        print("N must be at least 4")
        exit(1)


    solve_nqueens(N)
	
