"""
Name: Guage Schneider
File: tictactoe.py

Purpose: create a playable tic tac toe board
"""
import random

def main():
    board = the_board()
    player = next_player("")

    print("Hello friends and thanks for coming around to the gaaaaaaame! Let's get to it!")

    while not (winner_dinner(board) or draw_masters(board)):
        nice = niceties()
        
        display_board(board)
        whos_turn(player, board, nice)
        player = next_player(player)
    display_board(board)
    print("Good game! Thanks for playing!")


def the_board():
    """Creates the board itself.
    Parameters: none
    """
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    """Fills the board.
    Parameters: the square board
    """
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw_masters(board):
    """Gives the info on drawwwwwwwwwww
    Parameters: the square board
    """
    for square in range(9):
        if board[square] != "o" and board[square] != "x":
            return False
    print("It's a DRAW! WE'RE DRAWING PEOPLE, WE'RE DRAWING!")
    return True

def winner_dinner(board):
    """Gives the info on winner
    Parameters: the square board
    """
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def next_player(current):
    """Gives who is playing next
    Parameters: current
    """
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def whos_turn(player, board, nice):
    square = int(input(f"{player}, you're up! Choose a square (1-9): "))
    board[square - 1] = player
    print(nice)

def niceties():
    """Provides a random compliment on every move.
    Parameters: none
    """
    compliments = ["Nice move!", "Good work!", "You snuck that one in there, didn't you?", "Beautifully done!",\
         "Look out, RULER of Tic-Tac-Toe coming through!", "*clicks tongue* Noice.", "That was so good!", "I'm proud of you for that one."]

    compliment = random.choice(compliments)
    return compliment



if __name__ == "__main__":
    main()