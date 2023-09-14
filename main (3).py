class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Creating objects and calling the play() method
batsman = Batsman()
bowler = Bowler()

batsman.play()  # Output: "The batsman is batting."
bowler.play()   # Output: "The bowler is bowling.