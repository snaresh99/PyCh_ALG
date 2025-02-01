"""
* Define a new type called BankAccount that takes a single instance attribute
initial_baslance (defaults to 0)

> This type should support deposit() and withdraw() methods, which in turn should only support transactions
amounts, i.e., an attempt to deposit or withdraw -2$ should be ignored.

> Define 3 more specialized types of BankAccount with the following characteristics
1. Savings: has pay_interest() metho which deposits directly into the account when called;
interest rate: 0.0035

2. HighInterest: like Savings, but higher interest and with a withdrawl fee.
the fee is specified at initializaion and default to $5.
it is taken from the account balance from every withdrawl.
interest rate  = 0.007

3. Lockedin: like high interest, but higher interest without the ability to withdraw on demaind.
interest rate : 0.009

4.  The balance of any of the above accounts should be available by attribute access syntax
e.g., account_balance.

5. The representation of any of the instances should simply indicate the type of account
and the amount contained within 
"""

class BankAccount:
    """ A regular bank account """
    def __init__(self, initial_balance=0):
        self._balance = initial_balance # _balance is a private attribute.
        # requirement number 4 indicates that balance should be available by attribute access
        # its a good idea to define a balance property
        # this will be read only property

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw ${amount}")

    def __repr__(self):
        #instance_name = "savingsBankAccount", "HighInterestSavingsBankAccount" or "LockedInBankAccount"
        # __mro__ -> will give us the full inheritance chain in a tuple, so it i'll give
        # if our self is high interest savings bank, it ill give us high interst savings bank account and then object
        # __mro__ -> (Tuple of class names in the full inheritance chain leading upto object)
        intance_name = "".join([t.__name__ for t in type(self).__mro__[:-1]]) # give us all the objects excluding the last one.
             
        return f"A ${intance_name}  with ${self.balance} in it"
    
    @property
    def balance(self):
        return self._balance
        
    
class Savings(BankAccount):
    """ like a bank account, but interest earning account."""
    interest = 0.0035

    def pay_interst(self):
        interest_earned = round(self.balance * self.interest, 2)
        self.deposit(interest_earned)


# Requirement 2: High Interest:

class HighInterest(Savings):
    """ like a savings account, but earning higher interest in exchage for 
    withdrawler fees """

    interest = 0.007

    def __init__(self, initial_balance=0, withdrawl_fee = 5):
        super().__init__(initial_balance)
        self.withdrawl_fee = withdrawl_fee
    
    def withdraw(self, amount):
        if 0 < amount + self.withdrawl_fee <= self.balance:
            self._balance = self.withdrawl_fee
            super().withdraw(amount)

class LockedIn(HighInterest):
    """ like a high interest saving account but earning higher interest,
    in exchange for the ability to withdraw early """

    interest = 0.009

    def withdraw(self, amount):
        return f" can't make early withdrawl from a locked in savings account"


