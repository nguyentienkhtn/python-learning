import random


class Coin:

    def __init__(self):
        self.__side = 'Heads' # side is a private atttribute

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__side = 'Heads'
        else:
            self.__side = 'Tails'

    def get_side(self):
        return self.__side


def main():
    my_coin = Coin()
    print(my_coin.get_side())
main()

