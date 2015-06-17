__author__ = 'Tiger'

def probability(x, y, n):
    board = [[0 for x in range(8)] for x in range(8)]
    #(1, 1) signifies upper right corner
    x -= 1
    y -= 1
    #set start state, 100% probability
    board[x][y] = 1
    print_board(board)
    for nth_move in range(0, n):
        next_board = [[0 for x in range(8)] for x in range(8)]
        #check every square on the board. If it's possible to move to this square, mark this square with
        #the probability the knight moves here (source square prob/8)
        for i in range(8):
            for j in range(8):
                square_prob = 0
                #check the 8 possible source squares
                #up-right
                if i - 2 >= 0 and j + 1 < 8:
                    square_prob += board[i - 2][j + 1] / 8
                #up-left
                if i - 2 >= 0 and j - 1 >= 0:
                    square_prob += board[i - 2][j - 1] / 8
                #down-right
                if i + 2 < 8 and j + 1 < 8:
                    square_prob += board[i + 2][j + 1] / 8
                #down-left
                if i + 2 < 8 and j - 1 >= 0:
                    square_prob += board[i + 2][j - 1] / 8
                #right-up
                if j + 2 < 8 and i - 1 >= 0:
                    square_prob += board[i - 1][j + 2] / 8
                #right-down
                if j + 2 < 8 and i + 1 < 8:
                    square_prob += board[i + 1][j + 2] / 8
                #left-up
                if j - 2 >= 0 and i - 1 >= 0:
                    square_prob += board[i - 1][j - 2] / 8
                #left-down
                if j - 2 >= 0 and i + 1 < 8:
                    square_prob += board[i + 1][j - 2] / 8
                next_board[i][j] = square_prob
        board = next_board
        print("\n")
        print_board(board)
    return sum(map(sum, board))

def print_board(board):
    for row in board:
        print(row)

print(probability(1, 1, 2))
print(probability(4, 4, 1))
print(probability(2, 3, 10))
print(probability(4, 3, 50))