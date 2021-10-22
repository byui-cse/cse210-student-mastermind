import random


class Guess:
    """The responsibility of Board is to keep track of the pieces in play.

    Attributes:
        board: A board is defined as a designated playing surface..
        
    """
    
    def __init__(self, name, number):
        self._prepare()
        self._name = name
        self._number = number
        self._hint = ""

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_hint(self):
        return self._hint

    
    def is_empty(self):
        pass
        
        
    '''def to_string(self):
        border = "--------------------"
        count = 0
        return f"" '''
   
    def _prepare(self):
        pass
    