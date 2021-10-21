
from game.board import Board
from game.console import Console
from game.guess import Guess
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        guess (Rabbit): An instance of the class of objects known as Guess.
        roster (Roster): An instance of the class of objects known as Roster.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """        
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._roster = Roster()
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """

        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
            self._board.prepare(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # Display Game Board
        board = self._board.to_string()
        self._console.write(board)

        # Get Players next guess
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        player_guess = self._console.read_number("What is your guess?")
        guess = Guess(player_guess)
        player.get_guess(guess)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current guess.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        guess = player.get_guess()
        self._board.apply(guess)

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means giving players a hint.

        Args:
            self (Director): An instance of Director.
        """
        if self.mastermind.has_won(self.roster.get_current()):
            winner = self.roster.get_current()
            name = winner.get_name()
            print(f"\n{name} won!")
            self.keep_playing = False
        self.roster.next_player()
