'''Sophie Samuels, COP3410, Assignment 1, CreditCard.py exercises, 2.9.24'''

'''
COP3410 - Classes and OOP
Modelling a credit card class - Parts taken from "Data Structures and Algorithms in Python"

'''


################ Parent class of any credit card ##############################

class CreditCard:
    '''A consumer credit card.'''  # docstring, the first set of comments after the name of class is considered the help for that class. help(CreditCard)

    ##R7
    def __init__(self, customer, bank, acnt, limit, balance=0):  # The constructor is the very first method
        '''Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt : the acount identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        '''
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance  # we start with a balance of zero, this is private, nobody can change it

    def get_customer(self):  # The get functions are a must, they're called accessor functions (methods)
        '''Return name of the customer.'''
        return self._customer

    def get_bank(self):
        '''Return the bank s name.'''
        return self._bank

    def get_account(self):
        '''Return the card identifying number (typically stored as a string).'''
        return self._account

    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit

    def get_balance(self):
        '''Return current balance.'''
        return self._balance

    def set_limit(self, limit):  # a setter would change the attribute values, we are allowing change to the limit
        self._limit = limit

    def charge(self, purchase):
        '''
        A modification to charge method that would also decrement the limit
        '''
        ##R5
        if not isinstance(purchase, (int, float)):
            raise TypeError("Purchase amount must be a number.")

        if (purchase + self._balance) <= self._limit:
            self._balance += purchase
            self._limit -= purchase
            return True
        else:
            return False

    def make_payment(self, payment):
        '''Process customer payment that reduces balance.'''
        ##R5
        if not isinstance(payment, (int, float)):
            raise TypeError("Payment amount must be a number.")
        ##R6
        if payment < 0:
            raise ValueError("Payment cannot be a negative number.")

        self._balance -= payment

    ##C30 establishing a nonpublic method of set_balance
    ##we only need to place in superclass because the subclass with inherit the protected method
    def _set_balance(self, new_balance):
        self.balance = new_balance

    def __str__(self):
        """ Returns a string representation of self """
        return "\ncustomer: " + str(self._customer) + "\nbank: " + str(self._bank) + "\naccount: " + str(
            self._account) + "\nlimit: " + str(self._limit) + "\nbalance: " + str(self._balance)


############### Testing the class ########################################

if __name__ == "__main__":  # uses test cases to test the class inside the same script file

    wallet = []  # empty list will store three instances of creditcard (3 new credit cards)
    SS = wallet.append(CreditCard('Sophie Samuels', 'Bank of America', '5391 0375 9387 5309', 2500))
    TS = wallet.append(CreditCard('Thomas Samuels', 'Chase', '3485 0399 3395 1954', 3500))
    OS = wallet.append(CreditCard('Oliver Samuels', 'CitiBank', '5391 0375 9387 5309', 5000))

    for c in range(3):  # for all 3 cards make sure construction has been done properly
        print('Customer =', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Available Credit ', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())

    ##R8 The range for the loop was changed so that the charges accumulated until CARD 3 (ending in 5309 reached its...
    ##...credit limit of $5000 while the other cards continue to accumulate debt.
    for val in range(1, 42):
        wallet[0].charge(
            val)  # invoking a method to charge the cards all 3 of them multiple times, make sure the charges are accumulated
        print('Balance on card1 = ', 'round ', val, 'is: ', wallet[0].get_balance())
        wallet[1].charge(2 * val)
        print('Balance on card2 = ', 'round ', val, 'is: ', wallet[1].get_balance())
        wallet[2].charge(3 * val)
        print('Balance on card3= ', 'round ', val, 'is: ', wallet[2].get_balance())

    for c in range(3):  # making payments , does it go through? Does it change the balance?
        if wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print('New_balance = ', wallet[c].get_balance())
            print('Available_Credit = ', wallet[c].get_limit())

    # only achievable with __str__ method
    print(wallet[0])
    print(wallet[1])
    print(wallet[2])


################### Inheritance ########################################

class PredatoryCreditCard(
    CreditCard):  # a child of the credit card class, it is inheriting all the methods and it's allowed to use all the instances from Credit Card
    ''' An extension to CreditCard that compounds interest and fees '''

    def __init__(self, customer, bank, acnt, limit, apr):
        #C28: add attribute to set charge calls to zero
        self._charge_calls = 0
        # CreditCard. __init__ (self,customer, bank, acnt, limit) #use this technique or the one below
        super().__init__(customer, bank, acnt, limit)  # call super constructor, this is the CreditCard initializer
        self._apr = apr

    def get_apr(self):
        ''' Returns the APR on a creditcard '''
        return self._apr

    def charge(self, price):
        ''' Charge given price to the card, assuming sufficient credit limit.
            Return True if charge was processed.
            Return False and assess 5 fee if charge is denied.
        '''
        success = super().charge(price)  # call inherited method
        if not success:
            self._balance += 5  # assess penalty
        return success  # caller expects return value

    def process_month(self):
        '''Assess monthly interest on outstanding balance.'''
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)  # 1/12 power of (1+apr)
            self._balance = monthly_factor * self._balance
        ##C28 counter adds each charge call, once it reaches 10 it will add $1 to the balance
        self._charge_calls += 1
        if self._charge_calls > 10:
            self._balance += 1
        ##C29 assign minimum monthly payment, assess fee if not paid by end of cycle
        min_payment_percentage = 0.05
        min_payment = min_payment_percentage * self._balance
        if self._balance < min_payment:
            self._balance += 35 #late fee


    def __str__(self):
        """ Returns a string representation of self """
        return "\ncustomer: " + str(self._customer) + "\nbank: " + str(self._bank) + "\naccount: " + str(
            self._account) + "\nlimit: " + str(self._limit) + "\nbalance: " + str(self._balance) + "\nAPR: " + str(
            self._apr)


############### Testing the class ########################################

if __name__ == "__main__":  # uses test cases to test the class inside the same script file

    AmEx = PredatoryCreditCard('Larry Bird', 'NBA Bank', '1234 5678 9012 3456', 5000, 0.0825)  # calling the constructor

    print(AmEx)  # this shows the need for __str__ method

    print('\nAmEx charged $200:', AmEx.charge(200))
    AmEx.make_payment(100)
    AmEx.process_month()
    print(AmEx)
    print('\nAmEx charged $5000:', AmEx.charge(5000))
    AmEx.process_month()
    print(AmEx)








