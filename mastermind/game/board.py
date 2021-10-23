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
        attempt = guess

        for i in str(attempt):
            self._guesses.append(i)

        self.compare_guess()

    def compare_guess(self):
        '''The class compares the guesses and changes the asterisks list.

        Args:
            self (Board): an instance of Board.
        '''
        
        for i, args in enumerate(self._guesses):

            self._dashes[i] = str(args)

            if self._number[i] == self._guesses[i]:
                self._asterisks[i] = 'X'

            elif args in self._number and self._number[i] != self._guesses[i]:
                index_guesses = self._guesses.index(args)
                self._asterisks[index_guesses] = 'O'
            
            else:
                self._asterisks[i] = '*'

        print(self._number)

        self._guesses = []

    def to_string(self, roster):
        self_board = roster.players[0]._board
        opponent_board = roster.players[1]._board
        table = '\n----------------------------'

        table += f'\nPlayer {roster.players[0].get_name()}: {" ".join(self_board._dashes)}, {" ".join(self_board._asterisks)}'
        table += f'\nPlayer {roster.players[1].get_name()}: {" ".join(opponent_board._dashes)}, {" ".join(opponent_board._asterisks)}'
        table += '\n----------------------------'

        return table


    def _prepare(self):
        '''The protected method _prepare, adds 4 numbers between 1, 9 to guess.

        Args:
            self (Board): an instance of Board
        '''
        number = str(random.randint(1000, 9999))

        for i in number:
            self._number.append(i)


    def is_win(self):
        '''The class return true or false if the current player
        guesses everything.

        Args:
            self (Board): an instance of Board            
        '''

        if self._dashes == self._number:
            return True
        else:
            return False
