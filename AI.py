from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__("Cyborg")
    
    
    def choose_gesture(self):
        list_of_gesture_options = random.choice(self.gesture_choices)
        return list_of_gesture_options

        


