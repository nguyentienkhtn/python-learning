from coin import Coin


def main():
    my_coin = Coin()

    print("init side: ", my_coin.get_side())

    while True:
        my_coin.toss()
        print("random side: ", my_coin.get_side())


main()
