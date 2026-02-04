

from termcolor import colored
import os

def clear_screen():
    os.system("clear")

class Board:
    def __init__(self, size):
        self.size = size
        self.reset_board()


    def show_board(self, players):
        clear_screen()
        print("\n"*2)

        for i in range(0, self.size * self.size, self.size):
            row = []
            for cell in self.board[i:i + self.size]:
                colored_cell = cell
                for p in players:
                    if cell == p.char:
                        colored_cell = colored(cell, p.color)
                row.append(colored_cell)

            print(" | ".join(row))
            if i < (self.size - 1) * self.size:
                print("-" * ((self.size * self.size) + 1))


    def update_board(self, choice, symbol):
        index = choice - 1
        if self.is_valid_move(index):
            self.board[index] = symbol
            return True
        return False

    def is_valid_move(self, index):
        return 0 <= index < len(self.board) and self.board[index].isdigit()

    def reset_board(self):
        if self.size == 3 :
            self.board = [str(i) for i in range(1, self.size * self.size + 1)]
        else:
            self.board = [str(i).zfill(2) for i in range(1, self.size * self.size + 1)]

    def get_available_please(self):
        return [int(cell)for cell in self.board if cell.isdigit()]

