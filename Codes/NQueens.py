def n_queens(n, board=[]):
    if n == len(board):
        return 1
    
    cnt = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            cnt += n_queens(n, board)
        board.pop()
    
    return cnt

def is_valid(board):
    curr_queen_row, curr_queen_col = len(board)-1, board[-1]

    for row, col in enumerate(board[:-1]):
        diff = abs(curr_queen_col - col)
        if diff == 0 or diff == curr_queen_row - row:
            return False
        
    return True

for i in range(10):
    print(n_queens(i))
