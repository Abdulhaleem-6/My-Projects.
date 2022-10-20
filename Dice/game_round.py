import random 

class GameRound():
    def __init__(self, dice):
        self.dice = dice
        self.history = []
        self.min = 1
        self.max = 6

    def play(self):
        no1 = random.randint(self.min, self.max)
        no2 = random.randint(self.min, self.max)
        no3 = random.randint(self.min, self.max)
        result = [no1, no2, no3]

        self.history.append(result[-1])

    def roll(self):
        while True:
            print('''1.roll the dice    2.To exit ''')
            user = int(input("what you want to do?\n"))
            if user == 1 :
                self.dice._dice_faces
                self.history.append(self.dice._results[-1])

            else:
                break


            # self.history.append(self.dice._results[-1])