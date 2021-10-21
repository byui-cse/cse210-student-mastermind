import random

from game import roster

class Board:

    """
     A board is defined as a designated playing surface. The responsibility of Board is to keep track of the pieces in play.
    """

    def __init__(self) -> None:
        """
        The constructor declares and initializes instance attributes with their default values. It also invokes the private _prepare method
        """
        self._items = {}

    

    def prepare(self, player):
        """Sets up the board with an entry for each player.
        
        Args:
            self (Board): an instance of Board.
        """
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        guess = "----"
        hint = "****"
        self._items[name] = [code, guess, hint]

    def _create_hint(self, code, guess):
        """Generates a hint based on the given code and guess.

        Args:
            self (Board): An instance of Board.
            code (string): The code to compare with.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint  

    def to_string(self):
        """
        The to_string method converts the board data to its string representation and returns it to the caller.

        Args:
            self(Board): an instance of Board
        """
        text = "\n-------------------------\n"
        for key, value in self._items.items():
            text += f"Player {key}: {value[1]}, {value[2]}\n"
        text += "-------------------------\n"
        return str(text)

    def apply(self, guess):
        """
        The apply method applies a move to the playing surface. In this case, that means ???????? The apply method accepts one argument, an instance of Move.

        Args:
            self(Board): an instance of Board.
            move (Move): an instance of Move.
        """
        self.guess = guess.get_guess()

