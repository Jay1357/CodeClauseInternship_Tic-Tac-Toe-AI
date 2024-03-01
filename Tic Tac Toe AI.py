import random

def print_board(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "O"
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_move = None
    best_score = -float("inf")
    for move in available_moves(board):
        board[move[0]][move[1]] = "O"
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "X"
        else:
            print("AI is making a move...")
            move = get_best_move(board)
            board[move[0]][move[1]] = "O"

        if check_winner(board, "X"):
            print_board(board)
            print("X wins!")
            break
        elif check_winner(board, "O"):
            print_board(board)
            print("O wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
