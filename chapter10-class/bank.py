class Bank:

    def __init__(self, initBalance):
        self.__balance = initBalance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            print('Insufficient balance!!')
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return 'The balance ' + format(self.__balance, ',.2f')