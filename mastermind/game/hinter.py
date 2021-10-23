# from game.engine import Engine

class Hinter:

    def generate_hint(self, code, guess):
        # Starts by assuming everything is wrong
        hint = "****"

        # Trasform code, guess and output into lists
        code_list = list(code.strip(" "))
        guess_list = list(guess.strip(" "))
        hint_list = list(hint.strip(" "))

        for i in range(len(code_list)):
            # Replace with "o"
            if guess_list[i] in code_list:
                hint_list[i] = "o"
            
            # Replace with "x"
            # Watch out! some "o"s will be replaced with "x", that's why "x" comes last
            if guess_list[i] == code_list[i]:
                hint_list[i] = "x"

        # For testing
        # print(f"code:  {code_list}")
        # print(f"guess: {guess_list}")
        # print(f"hint:  {hint_list}")

        # Converts the output back into a string and returns it
        hint = "".join(hint_list)
        return hint

