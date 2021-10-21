class Guess:
    """A maneuver in the game. The responsibility of Move is to keep track of the players guesses.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The number guessed by current user.
        
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
            guess
        """
        self._guess = guess

    def get_guess(self):
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess

  