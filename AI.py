from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__("Cyborg")

    def choose_gesture(self):
        random.choice[self.gestures_choice]
        print (self.choice)
        
Cyborg = AI()
Cyborg.choose_gesture()