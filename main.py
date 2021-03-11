from user import User
import sys


def print_board(board):
    """
    Prints the board onto the console.
    """
    print(board["TOP-L"] + "|" + board["TOP-M"] + "|" + board["TOP-R"])
    print("-----")
    print(board["MID-L"] + "|" + board["MID-M"] + "|" + board["MID-R"])
    print("-----")
    print(board["BOT-L"] + "|" + board["BOT-M"] + "|" + board["BOT-R"])


def create_board():
    """
    Creates/Resets the board dictionary.
    """
    global board
    board = {
        "TOP-L": "1",
        "TOP-M": "2",
        "TOP-R": "3",
        "MID-L": "4",
        "MID-M": "5",
        "MID-R": "6",
        "BOT-L": "7",
        "BOT-M": "8",
        "BOT-R": "9"
    }


def get_user_names():
    """
    Asks both users for their name. Adds each user to the users list. Along with their symbols for the tictactoe.
    """
    global users
    users_list = ["first", "second"]
    for i in range(2):
        username = input("\nWhat is the name of the {} player? ".format(users_list[i]))
        while True:
            symbol = input("What symbol would you like to choose?(Please make it 1 character long) ")
            for x in users:
                if symbol == x.symbol:
                    symbol = "INVALID"
                    print("Please choose a different symbol from your opponent.")
            if len(symbol) == 1:
                break
        users.append(User(username, symbol))


def user_move(name):
    """
    Prompts user to move to a legal spot.
    """
    print_board(board)
    position = input("Which position would {} like to select?({}) ".format(name.name, name.symbol))
    while position not in board.values():
        print("The slot you chose was invalid.")
        position = input("Which position would {} like to select?({}) ".format(name.name, name.symbol))

    for k, v in board.items():
        if v == position:
            board[k] = name.symbol


def find_winner(name):
    """
    Checks if there is a winner.
    :returns: {boolean} True = there's a winner
    """
    symbol = name.symbol

    # Horizontal wins.
    if board["TOP-L"] == symbol and board["TOP-M"] == symbol and board["TOP-R"] == symbol: return True
    if board["MID-L"] == symbol and board["MID-M"] == symbol and board["MID-R"] == symbol: return True
    if board["BOT-L"] == symbol and board["BOT-M"] == symbol and board["BOT-R"] == symbol: return True

    # Vertical wins.
    if board["TOP-L"] == symbol and board["MID-L"] == symbol and board["BOT-L"] == symbol: return True
    if board["TOP-M"] == symbol and board["MID-M"] == symbol and board["BOT-M"] == symbol: return True
    if board["TOP-R"] == symbol and board["MID-R"] == symbol and board["BOT-R"] == symbol: return True

    # Diagonal wins.
    if board["TOP-L"] == symbol and board["MID-M"] == symbol and board["BOT-R"] == symbol: return True
    if board["TOP-R"] == symbol and board["MID-M"] == symbol and board["BOT-L"] == symbol: return True


def restart_game():
    """
    Asks the user if he wants to restart, if so run_game()
    """
    print("\n==============================================================")
    user_input = input("Type anything to continue or type '-1' if you'd like to exit. \n")
    if user_input == "-1":
        print("\n Thank you for playing my TictacToe game!")
        sys.exit()
    else:
        run_game()


def run_game():
    """
    Runs the game. Repeats if there is no winner.
    """
    create_board()
    for i in range(9):
        user_move(users[i % 2])

        if find_winner(users[i % 2]):
            print("\n{}({}) is the Winner!".format(users[i % 2].name, users[i % 2].symbol))
            print_board(board)

            restart_game()

        if i == 8:
            print("\nIt seems like there was no winner. ")
            restart_game()

    print_board(board)


# Data to hold the board and users.
board = {}
users = []

# Starting the game.
get_user_names()
run_game()