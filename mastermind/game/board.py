from math import log
import random


class Board:
    """The responsibility of Board is to keep track of the pieces in play.

    Attributes:
        board: A board is defined as a designated playing surface..
        
    """
    
    def __init__(self):
        self._secret_code = []
        self._prepare()
        self.last_guess = ""
        print(self._secret_code)        


    def apply(self, player):
        self.last_guess = str(player.get_guess().get_number()) #do guess
        status = player.get_status()
        # print(status)
        # for x in range(4):
        for num in range(4):
            if self.last_guess[num] == str(self._secret_code[num]):
                status[num] = 'x'
            elif status[num] == '*':
                result = self.last_guess.find(str(self._secret_code[num]))
                if result != -1:
                    status[num] = 'o'
        player.set_status(status)
        # print(status)
        
    def is_answered(self):
        # compare the last guess as string against the secret code (converted from a numbered list to a string)
        # if str(self.last_guess.get_number()) == "".join(str(num) for num in self._secret_code):
        if self.last_guess == "".join(str(num) for num in self._secret_code):
            return True
        return False
        
        
    def to_string(self, roster):        
        """Converts the board data to its string representation.

        Args:
           self (Board): an instance of Board.

        Returns:
            string: A representation of the current board.
        """
        text = "\n--------------------"
        for player in roster.players:
            text += (f"\nPlayer {player.get_name()}: {player.get_guess().get_number()}, ")
            for x in player.get_status():
                text += x
        text += "\n--------------------\n"
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
        self._secret_code[0] = (random.randint(1,9))        #why do we have 1-9, instead of 0-9 as the rest??
        self._secret_code[1] = (random.randint(0,9))
        self._secret_code[2] = (random.randint(0,9))
        self._secret_code[3] = (random.randint(0,9))
    
    