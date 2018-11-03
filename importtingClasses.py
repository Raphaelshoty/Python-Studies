from BuidingChildClasses import Account

class SavingsAccount(Account):
    pass

    def __init__(self,number,balance, credit = 0):
        Account.__init__(self,number, balance, credit)
    
    def getDetails(self):
        print("Savings details")
        print("Saving account number: ", getattr(self,'number'))
        print("Saving account balance: ", getattr(self,'balance'))

    
    def credit(self):
        return self.__credit
        
    def credit(self, credit):
        if(isinstance(self,SavingsAccount)):
            raise ValueError("SavingsAccount has no credit")
        

def main():
    savings = SavingsAccount(1,10000,0) # the credit is receiving 0 because a saving account will not have a credit
    savings.balance = 5000.50
    
    savings.credit(100)
    print(savings.credit)
    
    savings.getDetails()   

main()

