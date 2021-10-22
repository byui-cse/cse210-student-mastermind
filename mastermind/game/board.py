import random


class Board:
    """The responsibility of Board is to keep track of the pieces in play.

    Attributes:
        board: A board is defined as a designated playing surface..
        
    """
    
    def __init__(self):
        self._secret_code = []
        self._prepare()
        self.last_guess = 0
        print(self._secret_code)


    def apply(self, guess):
        self.last_guess = guess#do guess
        
        
    def is_answered(self):
        # compare the last guess as string against the secret code (converted from a numbered list to a string)
        if str(self.last_guess.get_number()) == "".join(str(num) for num in self._secret_code):
            return True
        return False
        
        
    def to_string(self):
        """border = "--------------------"
        return f"Player {self.last_guess.get_name()} {self.last_guess.get_number()} {self.last_guess.get_hint()}"
        count = 0
        return f"" """


        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        text = "\n--------------------"
        text += (f"Player {self.last_guess.get_name()} {self.last_guess.get_number()} {self.last_guess.get_hint()}")
        text += "\n--------------------"
        return text
   
    def _prepare(self):
        """ 
        Prepares the board with the secret code
        Args:
           self (Board): an instance of Board.

        Returns:
            _secredt_code: a four digit number represented as a list with 4 items.
            The code is a randomly generated, four digit number between 1000 and 9999.

        """
        self._secret_code = [0, 0, 0, 0]
        self._secret_code[0] = (random.randint(1,9))
        self._secret_code[1] = (random.randint(0,9))
        self._secret_code[2] = (random.randint(0,9))
        self._secret_code[3] = (random.randint(0,9))
    