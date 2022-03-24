import random

from Player import Player 


class Game:
    def __init__(self):
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
            pass
        elif user_input == 2:
            pass
        else:
            pass


    # def turn_order(self):
    #     random.choice[Players] # Players is a list, create a list of players
    #     print(f'Player {self.random.choice} has been chose to go first.')
    #     pass
    # 
    # 
   
   
game_go = Game()

game_go.rules()