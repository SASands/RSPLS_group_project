import random

from Human import Human
from AI import AI

class Game:
    def __init__(self):
        self.player_one = Human('John')
        self.player_two = Human('Mary')
        self.player_ai = AI()
        self.rps_ls = []
    
    
    def run_game(self):
        pass
    
    
    def welcome(self):
        print ("Welcome to Rock Paper Scissors Lizard Spock! Thanks for choosing to play RSPLS! Here are the Rules of engagement! Enjoy your game!  ")


    def rules(self):
        print ("1.The Game is played to best of three!-The first player to reach two wins, wins the Game."
                "2.Heres how to win-"
                   "-Rock crushes Scissors and Lizard"
                   "-Paper covers rock and disproves Spock."
                   "-Scissors cuts paper and decapitates Lizard."
                   "-Lizard eats Paper and poisons Spock."
                   "-Spock vaporizes Rock and smashes Scissors")


    def player_amount(self):
        user_input = input(f'Is there one or two players that are playing this game? Press  1  or  2    ')
        if user_input == 1:
            self.player_one.choose_gesture()
            self.rps_ls.append(self.player_one.choice)
            self.player_ai.choose_gesture()
            self.rps_ls.append(self.player_ai.choice)

            pass
    
        elif user_input == 2:
            pass
        else:
            pass

   
   
   
   
   
   
   
   
   
    def rock_beats(self):
        if self.rps_ls[0] == "rock" and self.rps_ls[1] == "scissors" or  self.rps_ls[1] == "lizard":

            print(f"{}}")
       
       
       
       
       
       
        # if Human().choice == "rock" and AI.choice == scissors or lizard:
        #     print(human wins!)
        #     Human.score += 1
       
    def paper_beats():
        pass
       

    def scissors_beats():
        pass

    def lizard_beats():
        pass

    def spock_beats():
        pass




    # def turn_order(self):
    #     random.choice[Players] # Players is a list, create a list of players
    #     print(f'Player {self.random.choice} has been chose to go first.')
    #     pass
    # 
    # 
   
