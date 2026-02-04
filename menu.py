from termcolor import colored
from pyfiglet import figlet_format
import os 
def clear_screen():
    os.system("clear")
    
class Menu:

    def menu_start (self):
         
        print((colored(figlet_format("Welcom In Tic Tac Toe Game"), color="blue")))
        while True:
            choice = input(
            "1. Start Game\n" 
            "2. Quit Game\n" 
            "Enter Choice 1 or 2 : ").strip()
            if choice in ('1','2'):
                return choice
            print(colored("Enter 1 or 2 Only","red"))


    def menu_end (self):
        print("\n")
        while True:
            choice = input(
            "1. Restart Game\n" 
            "2. Quit Game\n" 
            "Enter Choice 1 or 2 : ").strip()
            if choice in ('1','2'):
                return choice
            print(colored("Enter 1 or 2 Only","red"))

