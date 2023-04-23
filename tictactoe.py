import random

# Define the board
board = [[' ' for i in range(3)] for j in range(3)]

# Define the players
players = ['X', 'O']

# Define the current player
current_player = 0

# Define the game over flag
game_over = False

# Start the game loop
while not game_over:

    # Display the board
    for row in board:
        print(' '.join(row))

    # Get the player's move
    move = input('Enter your move (1-9): ')
    move = int(move) - 1

    # Check if the move is valid
    if move < 0 or move >= 9 or board[move // 3][move % 3] != ' ':
        print('Invalid move.')
        continue

    # Make the move
    board[move // 3][move % 3] = players[current_player]

    # Check for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            winner = board[row][0]
            game_over = True
            break

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            winner = board[0][col]
            game_over = True
            break

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]
        game_over = True

    # If there is a winner, announce the winner and end the game
    if game_over:
        print('The winner is {}!'.format(winner))
        break

    # Switch players
    current_player = (current_player + 1) % 2
