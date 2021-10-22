import random

class Board: 

    def __init__(self):
        '''The class constructor

        Args:
            self (Board): an instance of Board.
        '''

        self._number = []
        self._guesses = []
        self._asterisks = ['*', '*', '*', '*']
        self._dashes = ['-', '-', '-', '-',]
        self._prepare()

    def apply(self, guess):
        '''The class adds the guesses to the guess list.
        
        Args:
            self (Board): an instance of Board.
            guess (Guess): an instance of Guess
        '''
        attempt = guess.get_guess()

        for i in attempt:
            self._guesses.append(int(i))

    def compare_guess(self):
        '''The class compares the guesses and changes the asterisks list.

        Args:
            self (Board): an instance of Board.
        '''
        
        for i, args in enumerate(self._guesses):

            self._dashes[i] = args

            if self._number[i] == self._guesses[i]:
                self._asterisks[i] = 'X'

            elif args in self._number and self._number[i] != self._guesses[i]:
                index_guesses = self._guesses.index(args)
                self._asterisks[index_guesses] = 'O'
            
            else:
                self._asterisks[i] = '*'

        self._guesses = []

        
        print(self._asterisks)
        print(self._dashes)

    def _prepare(self):
        '''The protected method _prepare, adds 4 numbers between 1, 9 to guess.

        Args:
        self (Board): an instance of Board
        '''

        for _ in range(4):
            self._number.append(random.randint(1, 9))