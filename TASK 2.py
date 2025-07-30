import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    print()
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
    print()

def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

def is_draw():
    return ' ' not in board

def available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'X'):
        return 1
    elif is_winner(brd, 'O'):
        return -1
    elif ' ' not in brd:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in available_moves():
            brd[i] = 'X'
            score = minimax(brd, depth + 1, False)
            brd[i] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in available_moves():
            brd[i] = 'O'
            score = minimax(brd, depth + 1, True)
            brd[i] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = 'X'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'O' and the AI is 'X'.")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Your move (0-8): "))
            if board[move] != ' ':
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 0 to 8.")
            continue

        board[move] = 'O'
        print_board()

        if is_winner(board, 'O'):
            print("🎉 You win!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move = best_move()
        board[ai_move] = 'X'
        print_board()

        if is_winner(board, 'X'):
            print("😢 AI wins. Better luck next time!")
            break
        elif is_draw():
            print("It's a draw!")
            break

# Run the game
play_game()