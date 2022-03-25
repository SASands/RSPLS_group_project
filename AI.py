from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__("Cyborg")
    
    
    def choose_gesture(self):
        self.choice = random.choice(self.gesture_choices)
        print(f"Cyborg has chosen {self.choice}.")
        return self.choice
