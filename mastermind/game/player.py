class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last move.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _move (Move): The player's last move.
    """
    def __init__(self, name, board):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._guess = None
        self._board = board
        
    def get_guess(self):
        """Returns the player's last guess (an instance of Guess). If the player 
        hasn't guessed yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._guess

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name

    def set_guess(self, guess):
        """Sets the player's last move to the given instance of Move.

        Args:
            self (Player): an instance of Player.
            guess (Guess): an instance of Guess
        """
        self._guess = guess