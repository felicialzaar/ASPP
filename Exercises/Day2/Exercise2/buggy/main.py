from dicegame.runner import GameRunner


def main():
    print("Add the values of the dice")
    print("It's really that easy")
    print("What are you doing with your life.")
    #import ipdb; ipdb.set_trace()
    GameRunner.run()
    exit() #Fix: exit game when it's over or player stops.


if __name__ == "__main__":
    main()
