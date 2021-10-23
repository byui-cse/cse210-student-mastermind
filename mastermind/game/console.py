class Console:

    # Callable as many times as needed. Generics are importat as it is called: a) At the beginning, b) after P1 guessed, c) after P2 guessed
    def player_status(self, 
    p_one="Player 1", 
    p_two="Player 2", 
    g_one="----", 
    g_two="----",
    h_one="****",
    h_two="****"):
        
        print(f"""
--------------------
{p_one}: {g_one}, {h_one}
{p_two}: {g_two}, {h_two}
        """)


    def request_guess(self, player):
        print("--------------------")
        print(f"{player}'s turn:")

        guess = input("What is your guess? ")
        return guess