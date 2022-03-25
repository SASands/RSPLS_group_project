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
        self.welcome_rules
        self.player_amount()
        self.what_beats_what()
        self.champion()

    def start_more_games(self):
        self.player_amount
        self.what_beats_what
        self.champion

    def welcome(self):
        print ("Welcome to Rock Paper Scissors Lizard Spock! Thanks for choosing to play RSPLS! Here are the Rules of engagement! Enjoy your game!  ")


    def rules(self):
        print ("1.The Game is played to best of three!' \n '2.The first player to reach two wins, wins the Game.' \n '3.Heres how to win' \n ' -Rock crushes Scissors and Lizard' \n ' -Paper covers rock and disproves Spock.' \n ' -Scissors cuts paper and decapitates Lizard.' \n ' -Lizard eats Paper and poisons Spock.' \n ' -Spock vaporizes Rock and smashes Scissors")


    def welcome_rules(self):
        self.welcome
        self.rules

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


    def rock(self):
        if self.rpsls[0] == "rock" and self.rpsls[1] == "lizard" or self.rpsls[0] == "rock" and self.rpsls[1] == "scissors":
            print("Rocks wins!")
            self.player_one.score += 1
        elif self.rpsls[1] == "rock" and self.rpsls[0] == "lizard" or self.rpsls[1] == "rock" and self.rpsls[0] == "scissors":
            print("Rocks wins!")
            self.player_two.score += 1
        elif self.rpsls[1] == "rock" and self.rpsls[0] == "lizard" or self.rpsls[1] == "rock" and self.rpsls[0] == "scissors":
            print("Rock wins!")
            self.player_ai.score += 1

            
    def paper(self):
        if self.rpsls[0] == "paper" and self.rpsls[1] == "rock" or self.rpsls[0] == "paper" and self.rpsls[1] == "spock":
            print("Paper wins!")
            self.player_one.score += 1
        elif self.rpsls[1] == "paper" and self.rpsls[0] == "rock" or self.rpsls[1] == "paper" and self.rpsls[0] == "spock":
            print("Paper wins!")
            self.player_two.score += 1
        elif self.rpsls[1] == "paper" and self.rpsls[0] == "rock" or self.rpsls[1] == "paper" and self.rpsls[0] == "spock":
            print("Paper wins!")
            self.player_ai.score += 1

  


    def scissors(self):
        if self.rpsls[0] == "scissors" and self.rpsls[1] == "lizard" or  self.rpsls[0] == "scissors" and self.rpsls[1] == "paper":
            print("Scissors wins!")
            self.player_one.score += 1
        elif self.rpsls[1] == "scissors" and self.rpsls[0] == "lizard" or self.rpsls[1] == "scissors" and self.rpsls[0] == "paper":
            print("Scissors wins!")
            self.player_two.score += 1
        elif self.rpsls[1] == "scissors" and self.rpsls[0] == "lizard" or self.rpsls[1] == "scissors" and self.rpsls[0] == "paper":
            print("Scissors wins!")
            self.player_ai.score += 1



   
    def lizard(self):
        if self.rpsls[0] == "lizard" and self.rpsls[1] == "paper" or self.rpsls[0] == "lizard" and self.rpsls[1] == "spock":
            print("Lizard wins!")
            self.player_one.score += 1
        elif self.rpsls[1] == "lizard" and self.rpsls[0] == "paper" or self.rpsls[1] == "lizard" and self.rpsls[0] == "spock":
            print("Lizard wins!")
            self.player_two.score += 1
        elif self.rpsls[1] == "lizard" and self.rpsls[0] == "paper" or self.rpsls[1] == "lizard" and self.rpsls[0] == "spock":
            print("Lizard wins!")
            self.player_ai.score += 1




    def spock(self):
        if self.rpsls[0] == "spock" and self.rpsls[1] == "scissors" or self.rpsls[0] == "spock" and self.rpsls[1] == "rock":
            print("Spock wins!")
            self.player_one.score += 1
        elif self.rpsls[1] == "spock" and self.rpsls[0] == "scissors" or self.rpsls[1] == "spock" and self.rpsls[0] == "rock":
            print("Spock wins!")
            self.player_two.score += 1
        elif self.rpsls[1] == "spock" and self.rpsls[0] == "scissors" or self.rpsls[1] == "spock" and self.rpsls[0] == "rock":
            print("Spock wins!")
            self.player_ai.score += 1

    def same_gesture(self):
        if self.rpsls[0] == self.rpsls[1]:
            self.start_more_games

    def what_beats_what(self):
        self.rock()
        self.paper()
        self.scissors()
        self.lizard()
        self.spock()
        self.same_gesture()


    def champion(self):
        if self.player_one.score == 2:
            print("Player 1 WINS!!!")
        elif self.player_two.score == 2:
            print("Player 2 WINS!!!")
        elif self.player_ai == 2:
            print("Cyborg WINS!!!")
        while self.player_one.score != 2 or self.player_two.score != 2 or self.player_ai.score != 2:
            self.start_more_games()

    
            