
import random
 #this should generate a secret random number between 1000 and 9999
 #this is the number the players are trying to guess. 
 
class Code:

    def code_number(self):
        self.code = random.randint(1000,9999)
        return self.code