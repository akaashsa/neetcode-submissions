class Account:
    def __init__(self,title,balance):
        self.title = title
        self._balance = '$'+str(balance)
    def display_balance(self) -> None:
        print('Balance:',self._balance)


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
