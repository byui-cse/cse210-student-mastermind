from random import randint

class Coder:
    def __init__(self) -> None:
        self.random_code = str

    def generate_code(self):
        # The number is strigified because it will be checked and replace with string characters
        self.random_code = str(randint(1000, 9999))
        return self.random_code

