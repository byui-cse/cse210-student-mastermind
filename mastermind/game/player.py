class Player:

    # Generic function, can be called as many times
    def cleate_player(self, player_number) -> str:
        player = input(f"Enter a name for player {player_number}: ")
        return player


