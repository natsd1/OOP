class Account:
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder


    def deposit(self, amount_deposited: float):
        deposit = self.account_balance + amount_deposited

    def withdraw(self, amount_withdrawn: float):
        withdraw = self.account_balance - amount_withdrawn
        if self.account_balance > amount_withdrawn:
            print(True)
        else:
            print(False)

    def check_balance(self):
        return self.account_balance

my_account = Account(9068946114, 5000, "Stan")
my_account.deposit(100)
my_account.withdraw(9000)

print(my_account.check_balance())