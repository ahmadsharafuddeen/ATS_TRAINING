class TickTacToe:
    def __init__(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""]

    def display(self):
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print('__________')
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print('__________')
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == "":
            self.cells[cell_no] = player

    def is_winner(self, player):
        for i in range(10):
            if i == 1 or i == 4 or i == 7:
                if self.cells[i] == player and self.cells[i + 1] == player and self.cells[i + 2] == player:
                    return True
            if i == 1 or i == 2 or i == 3:
                if self.cells[i] == player and self.cells[i + 3] == player and self.cells[i + 6] == player:
                    return True
            if i == 1:
                if self.cells[i] == player and self.cells[i + 4] == player and self.cells[i + 8] == player:
                    return True
            if i == 3:
                if self.cells[i] == player and self.cells[i + 2] == player and self.cells[i + 4] == player:
                    return True

    def reset(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""]

board = TickTacToe()

def print_header():
    print('Welcome to Tic Tac Toe Game')

def refresh_screen():
    print_header()
    board.display()


while True:
    refresh_screen()

    # get X input
    x_choice = int(input("\n X) Please choose 1-9.>"))
    # Update board
    board.update_cell(x_choice, "X")

    # Refresh Screen
    refresh_screen()
    if board.is_winner("X"):
        print("\n X Wins! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    # get o input
    o_choice = int(input("\n O) Please choose 1-9.>"))
    # Update board
    board.update_cell(o_choice, "O")
    refresh_screen()
    if board.is_winner("O"):
        print("\n O Wins! \n")
        play_again = input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            continue
        else:
            break
