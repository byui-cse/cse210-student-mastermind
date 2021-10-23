import colorama
from colorama import Fore
colorama.init()

class Console:

    # Callable as many times as needed. Generics are importat as it is called: a) At the beginning, b) after P1 guessed, c) after P2 guessed
    def player_status(self, 
    p_one="Player 1", 
    p_two="Player 2", 
    g_one="----", 
    g_two="----",
    h_one="****",
    h_two="****"):
        
        print(f"""
--------------------
{Fore.MAGENTA}{p_one}: {g_one}, {h_one}{Fore.RESET}
{Fore.CYAN}{p_two}: {g_two}, {h_two}{Fore.RESET}
        """)


    def request_guess(self, player):
        print("--------------------")
        print(Fore.GREEN + f"{player}'s turn:" + Fore.RESET)

        guess = input(f"{Fore.YELLOW}What is your guess? {Fore.RESET}")

        # Validade if the player typed 4 numbers
        while len(guess) != 4:
            print(f"{Fore.RED}\nPlease type 4 numbers{Fore.RESET}")
            guess = input(f"{Fore.YELLOW}What is your guess? {Fore.RESET}")

        return guess