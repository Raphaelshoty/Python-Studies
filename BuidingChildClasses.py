##from classesTest import Pessoa 
##from classesTest import Account
##
##class SavingsAccount(Account):
##    pass
##
##    def __init__(self, firstName, lastName, balance, number, limitCred):
##        Account.__init__(self, number, balance, Pessoa(firstName, lastName))
##
##def main():
##    savingAccount = SavingsAccount("Raphael", "Lima", 1000, 1, 2000)
##    savingAccount.getDetails()
##
##main()
        
class Account:
    pass

    credit = 0
    number = 0
    balance = 0

    def __init__(self, number, balance, credit):
        self.__number = number
        self.__balance = balance
        self.__credit = credit

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self,number):
        if(number == None or not isinstance(number, int)):
            raise ValueError("Invalid number")
        else:
            self.__number = number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        if( isinstance(balance, str) or balance == None):
            raise ValueError("invalid value for Balance")
        else:
            self.__balance = balance

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self,credit):
        if( isinstance(credit, str) or credit == None ):
            raise ValueError("Invalid value for credit")
        else:
            self.__credit = credit

    def getDetails(self):
        print("Account Number: ", self.number)
        print("Account Balance: ", self.balance)
        print("Account Credit: ", self.credit)


    def deposit(self,amount):
        if(amount <= 0):                
            raise ValueError("Invalid deposit value")
        else:
            self.balance += amount            

    def withdraw(self, amount):
        if(amount > (self.credit + self.balance)):
            raise ValueError("Not enought funds")
        elif(amount < 0):
            raise ("Cannot deposit negative values")            
        elif(isinstance(amount, str)):
            raise ValueError("Not a number")
        else:
            self.balance -= amount
            self.credit -= self.balance
            
    def transfer(self, Account, amount):
        self.withdraw(amount)
        Account.deposit(amount)
        
        
        
##class SavingsAccount(Account):
##    pass
##
##    def __init__(self,number,balance, credit = 0):
##        Account.__init__(self,number, balance, credit)

##def main():
##    savings = SavingsAccount(1,10000)
##    savings.balance = 5000.50
##    savings.credit = 50.5
##    savings.getDetails()
##
##    setattr(savings,'balance',300)
##    savings.getDetails()
##
##main()
    
