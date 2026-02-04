
from board import Board
from player import Player
from menu import Menu
from level import Level
from termcolor import colored
from pyfiglet import figlet_format
import time
import os
import random


def clear_screen():
    os.system("clear")


class Game:
    def __init__(self):
        self.menu = Menu()
        self.level = None
        self.board = None
        self.players = []
        self.current = 0
        self.draw = 0
        self.mode = None

    def start(self):
        if self.menu.menu_start() == '1':
            self.part_game()
            self.game()
        else:
            self.quit_game()
    
    def part_game(self):
        while True:
            print (colored("-="*20,"blue"))
            mode_choice = input("1.player vs player\n2.player vs computer\nchoose 1 or 2:  ")
            if mode_choice in ('1','2'):
                self.mode = "AI" if mode_choice == '2' else "PvP"
                break

        self.create_players()


    def game(self):
 

        while True:
            print (colored("-="*20,"blue"))
            choice = input("1. Classic (3x3)\n2. Advanced (4x4)\nChoose: ")
            if not choice.isdigit() or choice not in ("1",'2'):
                print (colored("-="*20,"blue"))
                print (colored("Please Enter digit 1 or 2 only\n       Try again","red"))
                
                
            else:
                if choice == "1":
                    self.level = Level("Classic", 3, 3)
                else:
                    self.level = Level("Advanced", 4, 4)
                break
        
                    

        self.board = Board(self.level.size)
        self.play()
        time.sleep(3)
        clear_screen()
        if self.menu.menu_end() == "1":
            self.restart_game()
        else:
            self.quit_game()

    def create_players(self):
        used_names = []
        used_chars = []
        colors = ["blue","red"]
        if self.mode == 'PvP' :
            for i in range(2):
                while True:
                    print (colored("-="*20,"blue"))
                    name = input(f"Player {i+1} name (letter only) : ").strip()
                    char = input(f"Player {i+1} symbol (X or O or any letter): ").upper().strip()
                    print (colored("-="*20,"blue"))
                    name = self.format_input(name)

                    if not name.isalpha() or not char.isalpha() or len(char) != 1:
                        print(colored(" Invalid input ❌","red"))
                        print("please Enter Your information again")
                        print (colored("-="*20,"blue"))
                        continue
                    if name in used_names or char in used_chars:
                        print(colored("Name or symbol already used ❌","red"))
                        print("Player 2, please Enter your information again")
                        print (colored("-="*20,"blue"))
                        continue

                    self.players.append(Player(name, char,colors[i]))
                    used_names.append(name)
                    used_chars.append(char)
                    break
        else: 
                self.players.append(Player("Computer", "O", "red"))
                used_names.append("computer")
                used_chars.append("O")
                print (colored("Computer choosed 'O' to play with","cyan"))

                while True:
                    print (colored("-="*20,"blue"))
                    name = input(f"Player name (letter only) : ").strip()
                    char = input(f"Player symbol (X or  any letter): ").upper().strip()
                    print (colored("-="*20,"blue"))
                    name = self.format_input(name)

                    if not name.isalpha() or not char.isalpha() or len(char) != 1:
                        print(colored(" Invalid input ❌","red"))
                        print("please Enter Your information again")
                        print (colored("-="*20,"blue"))
                        continue
                    if name in used_names or char in used_chars:
                        print(colored("You cannot chose a name 'Computer' or symbol 'O'❌","red"))
                        print("Player , please Enter your information again")
                        print (colored("-="*20,"blue"))
                        continue

                    self.players.append(Player(name, char,"blue"))
                    used_names.append(name)
                    used_chars.append(char)
                    break
   

    def play(self):
        while True:
            self.board.show_board(self.players)
            player = self.players[self.current]
           
            if self.mode == "AI" and player.name == "Computer":
                print(colored("Computer is thinking...", "cyan"))
                time.sleep(1)
                choice = self.get_ai_move()
             
            else:
                        
                try:
                    start_time = time.time()
                    time_limit = 10 
                    print()
                    print(colored("You have 10 sec only choose fast","magenta"))
                    choice = int(input(f"\n{player.name} ({player.char}) choose: "))
                    

                    elapsed = time.time() - start_time

                    if elapsed > time_limit:
                        print(colored("⏰ Time's up! Turn skipped", "red"))
                        time.sleep(1)
                        self.current = 1 - self.current
                        continue

                    

                except ValueError:
                    print(colored(f"You Must enter number \n      Try again","red"))
                    time.sleep(1.5)
                    continue

            if choice not in range(1,(self.level.size*self.level.size)+1):
                print(colored(f"You Must enter number in [1 ,{self.level.size*self.level.size}]\n           Try again","red"))
                time.sleep(1.5)
                continue                

            if not self.board.update_board(choice, player.char):
                print(colored("The number is olready taken","red"))
                time.sleep(1.5)
                continue




            if self.check_win(player.char):
                self.board.show_board(self.players)
                print(colored(figlet_format(f"{player.name} WINS"), "yellow"))
                player.score += 1
                print(colored("SCORE", "yellow"))
                for p in self.players:
                    print(f"{p.name}: {p.score}")
                print(f"Drow: {self.draw}")
                break


        
            if self.check_draw():
                self.board.show_board(self.players)
                print(colored(figlet_format("Draw"), "green"))
                self.draw += 1 
                print(colored("SCORE", "yellow"))
                for p in self.players:
                    print(f"{p.name}: {p.score}")
                print (f"Draw: {self.draw}")
                break



            self.current = 1 - self.current

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def check_win(self, char):
        size = self.level.size
        win = self.level.win
        b = self.board.board

        # rows
        for r in range(size):
            count = 0
            for c in range(size):
                if b[r * size + c] == char:
                    count += 1
                    if count == win:
                        return True
                else:
                    count = 0

        # columns
        for c in range(size):
            count = 0
            for r in range(size):
                if b[r * size + c] == char:
                    count += 1
                    if count == win:
                        return True
                else:
                    count = 0

        # diagonals (simple)
        if all(b[i * (size + 1)] == char for i in range(win)):
            return True
        if all(b[(i + 1) * (size - 1)] == char for i in range(win)):
            return True

        return False
    
    def restart_game(self):
        self.board.reset_board()
        self.current = 0 
        self.game()


    def quit_game(self):
        print(colored(figlet_format("Thanks for playing"),"yellow"))


    def minimax(self,depth,is_maximizing,alpha, beta):
        
        if depth > 6: 
            return 0 
        
        if self.check_win(self.players[1].char):
            return 10 - depth
        if self.check_win(self.players[0].char):
            return depth - 10
        if self.check_draw():
            return 0 
        
        if is_maximizing:
            best_score = -float('inf')
            for move in self.board.get_available_please():
                original = self.board.board[move-1]
                self.board.board[move-1] = self.players[1].char
                score = self.minimax(depth+1,False,alpha,beta)
                self.board.board[move-1] = original
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        
        else:
            best_score = float('inf')
            for move in self.board.get_available_please():
                original = self.board.board[move -1]
                self.board.board[move -1] = self.players[0].char
                score = self.minimax(depth+1,True,alpha,beta)
                self.board.board[move-1] = original
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score


    def get_ai_move(self):
        
            for move in self.board.get_available_please():
                original = self.board.board[move-1]
                self.board.board[move-1] = self.players[1].char 
                if self.check_win(self.players[1].char):
                    self.board.board[move-1] = original 
                    return move 
                self.board.board[move-1] = original

            
            for move in self.board.get_available_please():
                original = self.board.board[move-1]
                self.board.board[move-1] = self.players[0].char
                if self.check_win(self.players[0].char):
                    self.board.board[move-1] = original
                    return move 
                self.board.board[move-1] = original

        
            return self.get_best_move()


    def get_best_move(self):
        best_score = -float('inf')
        best_moves = []


        for move in self.board.get_available_please():
            original = self.board.board[move-1]
            self.board.board[move-1] = self.players[1].char

            score = self.minimax(0,False,-float("inf"),float('inf')) 
            self.board.board[move-1] = original

            if score > best_score:
                best_score = score
                best_moves = [move]
            elif score == best_score:
                best_moves.append(move)

        return random.choice(best_moves)
        
    
    def format_input(self,text):
        formatted_text = "".join(word.capitalize() for word in text.split())
        return formatted_text
        
