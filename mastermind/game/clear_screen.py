import os
import platform
import time


class ClearScreen():
    """A code template for an object which interacts with the display.
    The responsibility of this class of objects is to determine the 
    type of OS and clear the screen accordingly.
    
    Stereotype:
        Interfacer
    
    Attributes:
        self.system (string): A string containing the OS.
        self.clear (string):  A string with the command to clear the screen.
    """

    def __init__(self) -> None:
        """The class constructor.
        
        Args:
            self (ClearScreen): an instance of ClearScreen.
        """
        self.__system = platform.system()
        self.__clear = ""

    def clear_screen(self):
        """Clears the screen with the right command depending
        on the OS.
        
        Args:
            self (ClearScreen): an instance of ClearScreen.
        """
        time.sleep(1)
        #if Windows:
        if self.__system == 'Windows':
            self.__clear = lambda: os.system("cls")
        #if Linux:
        else:
            self.__clear = lambda: os.system("clear")

        self.__clear()