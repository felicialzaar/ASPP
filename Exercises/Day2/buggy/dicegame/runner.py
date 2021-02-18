from .die import Die
#from .utils import i_just_throw_an_exception #Fix: not necessary.
from .die import roll #Fix: import roll method.

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            #total += 1
            total += die.value #Fix: count values, not dice. 
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        #c = 0
        consecutive_wins = 0 #Fix: clear variable name.
        runner = cls()  #Fix: create runner once, not every turn.
        dice = runner.dice  #Fix: create dice once, not every turn.
        while True:
            #runner = cls() 
            print("Round {}\n".format(runner.round))
           
            #for die in runner.dice: 
            for die in dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                consecutive_wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                consecutive_wins = 0
                
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if consecutive_wins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                roll(dice) #Fix: roll existing dice instead of recreating.
                continue
            else:
                #i_just_throw_an_exception()
                print("k bye") #Fix: stop game insted of throwing exeption.
                break;
