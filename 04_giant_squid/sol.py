import numpy as np
import sys

def hit(board: np.ndarray, coords: tuple[int, int]) -> bool:
    row_hit = True
    col_hit = True
    for i in range(0, 5):
        if board[coords[0], i] != 1:
            row_hit = False
        if board[i, coords[1]] != 1:
            col_hit = False
        if not (row_hit or col_hit):
            return False
    return True

def sumUnmarked(board: np.ndarray, marks: np.ndarray) -> int:
    return np.sum(board[marks == 0])

def bingo(called: list[int], boards: list[list[list[int]]]) -> int:
    # generate boolean hit arrays
    bools = [np.zeros((5, 5), dtype=int) for i in range(len(boards))]
    # np-ify each board
    boards = [np.array(board, dtype=int) for board in boards]

    for call in called:
        for idx, board in enumerate(boards):
            c = np.where(board == call)
            if len(c[0]) == 0:
                continue
            elif len(c[0]) == 1:
                # update boolean array
                coords = (c[0][0], c[1][0])
                bools[idx][coords[0], coords[1]] = 1
                if hit(bools[idx], coords):
                    return sumUnmarked(board, bools[idx]) * call

            else:
                print("more than one match")
                return -1
    return -1

def bingo2(called: list[int], boards: list[list[list[int]]]) -> int:
    # generate boolean hit arrays
    bools = [np.zeros((5, 5), dtype=int) for i in range(len(boards))]
    # np-ify each board
    boards = [np.array(board, dtype=int) for board in boards]
    yet_to_win = [i for i in range(len(boards))]

    for call in called:
        new_yet_to_win = yet_to_win.copy()
        for idx in yet_to_win:
            board = boards[idx]
            c = np.where(board == call)
            if len(c[0]) == 0:
                continue
            elif len(c[0]) == 1:
                # update boolean array
                coords = (c[0][0], c[1][0])
                bools[idx][coords[0], coords[1]] = 1
                if hit(bools[idx], coords):
                    new_yet_to_win.remove(idx)
                    if len(new_yet_to_win) == 0:
                        # found last
                        return sumUnmarked(board, bools[idx]) * call
            else:
                print("more than one match")
                return -1
        yet_to_win = new_yet_to_win

    return -1


if __name__ == "__main__":
    called = []
    boards = []
    with open(sys.argv[1], 'r') as file:
        called = file.readline()[:-1].split(',')
        called = list(map(lambda s: int(s), called))
        # remove the empty line
        file.readline()

        board = []
        for line in file:
            if len(line) == 1:
                # encountered readline; flush board 
                boards.append(board)
                board = []
            else:
                # continue board
                board.append(list(map(lambda s: int(s), line.split())))
        boards.append(board)

    print(bingo(called, boards))
    print(bingo2(called, boards))
