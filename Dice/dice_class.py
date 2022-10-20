import random

class Dice():
    def __init__(self):
        self.min = 1
        self.max = 6

    def roll(self):
        while True:
            print('''1.roll the dice    2.To exit ''')
            user = int(input("what you want to do?\n"))
            if user == 1 :
                self._dice_faces

            else:
                break    
    
    @property
    def _dice_faces(self):
        for element in self._results:

            if element == 1:
                print("[-----]")
                print("[     ]")
                print("[  0  ]")
                print("[     ]")
                print("[-----]")
            if element == 2:
                print("[-----]")
                print("[ 0   ]")
                print("[     ]")
                print("[   0 ]")
                print("[-----]")
            if element == 3:
                print("[-----]")
                print("[     ]")
                print("[0 0 0]")
                print("[     ]")
                print("[-----]")
            if element == 4:
                print("[-----]")
                print("[0   0]")
                print("[     ]")
                print("[0   0]")
                print("[-----]")
            if element == 5:
                print("[-----]")
                print("[0   0]")
                print("[  0  ]")
                print("[0   0]")
                print("[-----]")
            if element == 6:
                print("[-----]")
                print("[0 0 0]")
                print("[     ]")
                print("[0 0 0]")
                print("[-----]")
        

        
    @property
    def _results(self):
        no1 = random.randint(self.min, self.max)
        no2 = random.randint(self.min, self.max)
        no3 = random.randint(self.min, self.max)
        result = [no1, no2, no3]

        return result
