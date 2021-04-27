import bank


def main():

    my_account = bank.Bank(1500)
    print('Init balance: ', my_account.get_balance())
    my_account.deposit(500)
    print('balance: ', my_account.get_balance())
    print(my_account)

main()

