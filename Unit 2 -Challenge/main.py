class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance):
    self._account_number = account_number 
    self._account_holder_name = account_holder_name  
    self._account_balance = initial_balance 

  def deposit(self, amount):
    if amount > 0:
      self._account_balance += amount
      print(f"\nDeposited ${amount}. New balance: ${self._account_balance}")
    else:
      print("\nInvalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
    if amount > 0:
      if amount <= self._account_balance:
        self._account_balance -= amount
        print(f"\nWithdrew ${amount}. New balance: ${self._account_balance}")
      else:
        print("\nInsufficient funds to withdraw.")
    else:
      print("\nInvalid withdrawal amount. Please withdraw a positive amount.")

  def display_balance(self):
    print(
        f"\nAccount Balance for {self._account_holder_name}: ${self._account_balance}"
    )


account = BankAccount("123456789", "John Doe", 1000)


account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500) 
account.display_balance()
