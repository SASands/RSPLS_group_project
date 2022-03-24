import random

from Human import Human
from AI import AI



class Game:
    def __init__(self):
        self.player_one = Human("Rafael")
        self.player_two = Human("Leonardo")
        self.player_ai = AI()
        self.rpsls = []
        
    def run_game(self):
        self.welcome()
        self.rules()
        self.player_amount()


    def welcome(self):
        print ("Welcome to Rock Paper Scissors Lizard Spock! Thanks for choosing to play RSPLS! Here are the Rules of engagement! Enjoy your game!  ")


    def rules(self):
        print ("1.The Game is played to best of three!' \n '2.The first player to reach two wins, wins the Game.' \n '3.Heres how to win' \n ' -Rock crushes Scissors and Lizard' \n ' -Paper covers rock and disproves Spock.' \n ' -Scissors cuts paper and decapitates Lizard.' \n ' -Lizard eats Paper and poisons Spock.' \n ' -Spock vaporizes Rock and smashes Scissors")


    def player_amount(self):
        user_input = int(input('Is there one or two players that are playing this game? Press 1 or 2-'     ))
        if user_input == 1:
            self.player_one.choose_gesture()
            self.rpsls.append(self.player_one.choice)
            self.player_ai.choose_gesture()
            self.rpsls.append(self.player_ai.choice)
        elif user_input == 2:
            self.player_one.choose_gesture()
            self.rpsls.append(self.player_one.choice)
            self.player_two.choose_gesture()
            self.rpsls.append(self.player_two.choice)
        else:
            print("There can only be two Players for this game(tell your third wheel, we're sorry) please choose again!")
            self.player_amount
    
   
