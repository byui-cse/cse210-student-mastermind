class Guess:
    """A maneuver in the game. The responsibility of Guess is to keep track of the guesses or attempts from the player.
    
    Stereotype: 
        Information Holder

    Attributes:
        _attempt (integer): The guess or attemps from the player.
        
    """
    def __init__(self, attempt):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._attempt = attempt
        

    def get_attempt(self):
        """Returns the guess from player.

        Args:
            self (Guess): an instance of Guess.
        """
        return self._attempt

    