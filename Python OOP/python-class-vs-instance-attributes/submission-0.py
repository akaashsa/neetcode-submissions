class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self,name,balance) -> None:
        self.name =name
        self._balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


    def get_balance(self):
        print(f"{self.name}'s balance: ${self._balance}")
    
    def get_total_accounts():
        print(f"Total Accounts: {BankAccount.total_accounts}")

    def get_total_balance():
        print(f"Total Balance: ${BankAccount.total_balance}")
        pass


# TODO: Create two accounts

alice = BankAccount("Alice",1000)
bob = BankAccount("Bob",2000)
# TODO: Print the information using the mentioned format

alice.get_balance()
bob.get_balance()
BankAccount.get_total_accounts()
BankAccount.get_total_balance()