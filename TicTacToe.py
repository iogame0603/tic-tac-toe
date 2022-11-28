def clearBoard():
    global board

    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()


def printBoard(pos: int, turn: str):
    for i in range(3):
        for j in range(3):
            if board[i][j] == pos:
                board[i][j] = turn
            print(board[i][j], end=' ')
        print()


def changeTurn(turn: str):
    if turn == 'O':
        return 'X'
    else:
        return 'O'


def check(board, turn, turn_cnt):
    if (board[0][0] == turn and board[1][0] == turn and board[2][0] == turn)\
        or (board[0][1] == turn and board[1][1] == turn and board[2][1] == turn)\
        or (board[0][2] == turn and board[1][2] == turn and board[2][2] == turn)\
        or (board[0][0] == turn and board[0][1] == turn and board[0][2] == turn)\
        or (board[1][0] == turn and board[1][1] == turn and board[1][2] == turn)\
        or (board[2][0] == turn and board[2][1] == turn and board[2][2] == turn)\
        or (board[0][0] == turn and board[1][1] == turn and board[2][2] == turn)\
        or (board[2][0] == turn and board[1][1] == turn and board[0][2] == turn):
        return turn

    elif turn_cnt == 9:
        return "Draw"

clearBoard()
turn = 'O'
turn_cnt = 0

while True:
    try:
        pos= int(input(f"{turn}님의 차례: "))
    except ValueError:
        continue

    printBoard(pos, turn)
    turn_cnt += 1
    winner = check(board, turn, turn_cnt)
    
    if winner != None and winner != "Draw":
        print(f"{winner} is Win!")
        break
    elif winner == "Draw":
        print("Draw!")
        break

    turn = changeTurn(turn)