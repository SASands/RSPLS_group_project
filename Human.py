from Player import Player 

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    
   
    def choose_gesture(self):
        user_input = input('What gesture would you like to throw out?')
        print('Rock, Paper, Scissors, Lizard, Spock')
        self.choice = user_input
        return self.choice    


player_one = Human()

player_one.choose_gesture