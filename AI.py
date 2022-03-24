from Player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__("Cyborg")
    
    
    def choose_gesture(self):
        self.choice = random.choice(self.gesture_choices)
<<<<<<< HEAD
        print(f"Cyborg has chosen {self.choice}.")
        return self.choice
=======
        return self.choice

        

>>>>>>> f50fa6cf4e647a721e64fcc6f16938d094f3df01
