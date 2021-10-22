from game.board import Board
from game.console import Console
from game.player import Player
from game.roster import Roster
from game.code import Code
from game.guess import Guess

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """
#we are supposed to be protecting many of these methods and I haven't chosen any i thought the team
#should choose. 
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()
        self.number_players = 2 #there can only be two players at a time

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
        """Prepares the game before it begins. In this case, that means getting the player names
         and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(self.number_players):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(name)
            self.board.prepare(name)
    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        board = self.board #I haven't named anything in board  yet
        player=self.roster.get_current()

        # get next player's move
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")


        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        #I left the move in here from the last game, we don't have a class called Move,
        #but we might need one.
        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(move) #this is apply the hint. maybe call it apply_hint
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the guess is right and getting a hint if not. 


        Args:
            self (Director): An instance of Director.
        """
        
        
        #check if playersguess is == to random number generated at beginning. 

        #give hint hint comes from guess.py
     
       