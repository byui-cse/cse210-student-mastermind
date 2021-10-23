class Checker:

    def __init__(self) -> None:
        self.keep_playing = True

    # Compares the guess and the code of each player and decides
    def check_winner(self, 
    code,
    p_one,
    p_two,
    g_one,
    g_two):

        if g_one == code:
            print(f"{p_one} won!")
            self.keep_playing = False

        elif g_two == code:
            print(f"{p_two} won!")
            self.keep_playing = False

        else:
            self.keep_playing = True
