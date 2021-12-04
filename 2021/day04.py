import numpy as np

class BingoBoard:
    def __init__(self, board):
        self.board = board
    
    def sum_unmarked(self, calls):
        unmarked = filter(lambda item: item not in calls, self.board.A1)
        return sum(unmarked)

    def check_consecutive(self, row, calls):
        streak = 0
        for item in row:
            if item in calls: streak += 1
            else: streak = 0
        if streak == len(row): return True
        else: return False
    def check_bingo(self, calls):
        # horizontal bingos
        for row in self.board:
            if self.check_consecutive(row.A1, calls):
                return True # BINGO!
        # vertical bingos
        for row in self.board.T:
            if self.check_consecutive(row.A1, calls):
                return True # BINGO!
        # none sad
        else:
            return False

    def __str__(self):
        return str(self.board)

if __name__ == '__main__':
    ## INPUT STUFF
    f = open(__file__.replace(".py", ".txt"), "r")
    text = f.read()
    lines = text.split("\n\n")
    
    bingo_call, bingo_boards = lines[0], lines[2:]
    
    calls = list(map(int, bingo_call.split(",")))
    
    boards = []
    for string_board in bingo_boards:
        # first replace handles single-digit bingo nums
        np_formatted_board = string_board \
            .replace("  ", " ") \
            .replace("\n", ";")
        np_board = np.matrix(np_formatted_board)
        board = BingoBoard(np_board)
        boards.append(board)
    

    test_board1 = boards[0]
    print(test_board1)
    print("calls", calls)
    # print(test_board1.check_bingo([95, 79, 98, 71]))
    # print(test_board1.sum_unmarked([80,25,62,79,91,70,76,61,98,97,17,75,23,71,30,21,52,29,20,54,32,12,31]))

    # output a mapping of boards to what point they get bingo
    breaker = False
    for turn in range(1, 1+len(calls)):
        curr_calls = calls[:turn]
        for i, board in enumerate(boards):
            bingo = board.check_bingo(curr_calls)
            if bingo:
                print("BINGO for", i)
                print(board)
                print("Current calls:", curr_calls)
                bingo_score = board.sum_unmarked(curr_calls)*curr_calls[-1]
                print(board.sum_unmarked(curr_calls))
                print(f"Bingo score is {bingo_score}")
                breaker = True
                break
        else:
            print(f"No bingos for {turn}th call.")
        if breaker:
            break

    # print(len(boards))
    # part 2
    bingo_map = []
    for board in boards:
        for turn in range(1, len(calls)+1):
            bingo = board.check_bingo(calls[:turn])
            if bingo:
                bingo_map.append(turn)
                break
        else:
            bingo_map.append(float('inf'))

    for i, val in enumerate(bingo_map):
        if val == max(bingo_map):
            print("Worst board to pick is:")
            print(boards[i])
            bingo_score = calls[val-1]*(boards[i].sum_unmarked(calls[:val]))
            print(f"It wins on turn {val} and its score is: {bingo_score}")
    
    print(bingo_map)
