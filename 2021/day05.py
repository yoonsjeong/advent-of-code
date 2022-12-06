import numpy as np
import numpy as np
from matplotlib import pyplot as plt


class Board:
    def __init__(self):
        self.board = np.zeros((2,2))
        self.segments = []
    
    def add_segment(self, x1, y1, x2, y2):
        if max(x1, y1, x2, y2) >= max(self.board.shape):
            diff = max(x1, y1, x2, y2) - max(self.board.shape) + 1
            self.board = np.pad(self.board, (0, diff))
        if y1 == y2: # horizontal
            for i in range(min(x1, x2), max(x1, x2) + 1):
                self.board[i, y1] += 1
        elif x1 == x2: # vertical
            for j in range(min(y1, y2), max(y1, y2) + 1):
                self.board[x1, j] += 1
        else:
            slope = self.get_slope(x1, y1, x2, y2)
            start, end = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
            if slope == 1:
                for i,j in zip(range(start[0], end[0]+1), range(start[1], end[1]+1)):
                    self.board[i, j] += 1
            elif slope == -1:
                for i,j in zip(range(start[0], end[0]+1), reversed(range(end[1], start[1]+1))):
                    self.board[i, j] += 1
        return

    def get_slope(self, x1, y1, x2, y2):
        x_delta, y_delta = x1 - x2, y1 - y2
        if x_delta == 0: return float('inf')
        else: return y_delta/x_delta
    
    def count_intersections(self):
        return np.count_nonzero(self.board > 1)

if __name__ == '__main__':
    ## INPUT STUFF
    f = open(__file__.replace(".py", ".txt"), "r")
    text = f.read()
    lines = text.split("\n")

    segments = []
    for line in lines:
        p1, p2 = line.split("->")
        x1, y1 = list(map(int,p1.split(",")))
        x2, y2 = list(map(int,p2.split(",")))
        segments.append((x1, y1, x2, y2))
    
    board = Board()
    for seg in segments:
        board.add_segment(*seg)

    part1 = board.count_intersections()
    print(f"Part 1 answer is {part1}")
    plt.imshow(board.board, interpolation='nearest')
    plt.show()