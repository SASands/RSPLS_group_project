from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__("Cyborg")
    
    
    def choose_gesture(self):
        self.choice = random.choice(self.gesture_choices)
        return self.choice

        

