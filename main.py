import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, True))
                    board[i][j] = " "
        return best


def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def human_vs_human(board):
    players = ["X", "O"]
    current = 0
    print_board(board)

    while True:
        try:
            r, c = map(int, input(f"Player {players[current]} (row col): ").split())
        except ValueError:
            continue

        if not (0 <= r <= 2 and 0 <= c <= 2) or board[r][c] != " ":
            continue

        board[r][c] = players[current]
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        current = 1 - current


def human_vs_ai(board):
    print_board(board)

    while True:
        try:
            r, c = map(int, input("Your move (row col): ").split())
        except ValueError:
            continue

        if not (0 <= r <= 2 and 0 <= c <= 2) or board[r][c] != " ":
            continue

        board[r][c] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        i, j = ai_move(board)
        board[i][j] = "O"
        print("Computer move:")
        print_board(board)

        if check_winner(board) == "O":
            print("Computer wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("1. Human vs Human")
    print("2. Human vs Computer")
    choice = input("Choose mode (1 or 2): ")

    if choice == "1":
        human_vs_human(board)
    elif choice == "2":
        human_vs_ai(board)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    tic_tac_toe()
