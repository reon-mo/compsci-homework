class BankAccount:
    def __init__(self, forename, surname, starting_balance=0):
        self._forename = forename
        self._surname = surname
        self._balance = starting_balance
        self._transaction_history = []

    def get_forename(self):
        return self._forename

    def set_forename(self, new_forename):
        self._forename = new_forename
        print("Forename set to:", self._forename)

    def get_surname(self):
        return self._surname

    def set_surname(self, new_surname):
        self._surname = new_surname
        print("Surname set to:", self._surname)

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance
        print("Balance set to:", self._balance)    

    def deposit(self, amount):
        self._balance += amount
        print("Deposited:", amount)
        print("New balance:", self._balance)

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print("Withdrew:", amount)
            print("New balance:", self._balance)

class transaction:
    def __init__(self, forname, surname, starting_balamce=0):    
        if self._transaction_history == []:
            print ("no transaction history")
        super().__init__(self,)
        def get_transaction_history(self): 
            return self._transaction_history
    

account1 = BankAccount("James-Renz", "Shrimpton", 0)
account1.deposit(500)
account1.withdraw(200)
print("Current balance:", account1.get_balance())
print("Transaction history:", account1.get_transaction_history())
