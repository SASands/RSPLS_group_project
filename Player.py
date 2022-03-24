

class Player:
    def __init__(self, name):
        self.name = name
        self.gesture_choices = ['rock','paper','scissors','lizard', 'spock']
        self.choice = ''
        self.score = 0