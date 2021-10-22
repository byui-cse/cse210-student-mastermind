class Player:
    """A person taking part in a game. The responsibility of Player 
    is to keep track of their identity.
    
    Stereotype: 
        Information Holder

    Attributes:
        Encapsulated 
        __name (string): The player's name.
        
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
            __name(private): protect the player's name
        """
        self.__name = name
                
    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self.__name