from Player import Player 

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
   
    def choose_gesture(self):
        print("Here are your options for Gestures to throw!' \n 'Rock, Paper, Scissors, Lizard, Spock. ")
        user_input = input('What gesture would you like to throw out?')
<<<<<<< HEAD
        self.choice = user_input
        return self.choice
=======
        self.choice = user_input.lower()
        return self.choice    


player_one = Human("Player One")

player_one.choose_gesture()

>>>>>>> f50fa6cf4e647a721e64fcc6f16938d094f3df01
