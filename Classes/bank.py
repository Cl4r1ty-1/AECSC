class BankAccount:
    def __init__(self, user, balance):
        self.user = user
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
my_account = BankAccount("Alice", 1000)

print(my_account.user)
print(my_account.__balance)