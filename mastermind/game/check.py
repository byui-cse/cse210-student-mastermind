class Check:
    """A code template for.... The responsibility of Check
    is to ....
    
    Stereotype: 
        Information Holder

    Attributes:
        self.__okay (boolean): Default to True, return False 
                                when conditions not met.
    """

    def __init__(self):
        """
        """
        self.__okay = True

    def _compare_codes(self, player, board):
        """
        """
        if board._items[player][0] == board._items[player][1]:
            return self.__okay
        else:
            return not self.__okay

    def _check_input(self, guess):
        """
        """
        for digit in guess:
            if not digit.isdigit():
                print("\nHint: Only digits accepted.")
                return not self.__okay

        if len(guess) != 4:
            print(f"\nHint: You must enter 4 digits.")
            return not self.__okay

        return self.__okay