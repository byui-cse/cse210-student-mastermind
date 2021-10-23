from game.console import Console
from game.coder import Coder
from game.player import Player
from game.hinter import Hinter
from game.checker import Checker

class Director:

    def __init__(self) -> None:
        self.console = Console()
        self.coder = Coder()
        self.player = Player()
        self.hinter = Hinter()
        self.checker = Checker()

    def start_game(self):
        
        player_one = self.player.cleate_player(1)
        player_two = self.player.cleate_player(2)
        
        code = self.coder.generate_code()

        # Call one outside the loop as an intro
        self.console.player_status(player_one, player_two)

        while self.checker.keep_playing:

            # P1 data and status
            guess_one = self.console.request_guess(player_one)
            hint_one = self.hinter.generate_hint(code, guess_one)
            self.console.player_status(
                p_one=player_one, 
                p_two=player_two, 
                g_one=guess_one, 
                h_one=hint_one)

            # P2 data and overall status
            guess_two = self.console.request_guess(player_two)
            hint_two = self.hinter.generate_hint(code, guess_two)
            self.console.player_status(
                p_one=player_one, 
                p_two=player_two, 
                g_one=guess_one, 
                g_two=guess_two, 
                h_one=hint_one, 
                h_two=hint_two)

            # Check if somebody won
            self.checker.check_winner(
                code,
                player_one,
                player_two,
                guess_one,
                guess_two)