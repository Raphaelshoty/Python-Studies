from BuidingChildClasses import Account

class SavingsAccount(Account):
    pass

    def __init__(self,number, balance, credit = 0):
        Account.__init__(self,number,balance,credit)

    
    def getDetails(self):
        print("Savings Number: ", self.number)
        print("Savings Balance: ", self.balance)    
                

class CheckingAccount(Account):
    pass

    def __init__(self,number,balance,credit):
        Account.__init__(self,number,balance,credit)


def main():
    savings = SavingsAccount(1,1000,0)
    checking = CheckingAccount(2,15000,1000)

    print("Initial Accounts: ")
    print("Savings account: ")
    savings.getDetails()
    print("Checking account: ")
    checking.getDetails()

    print("\n")

    print("some deposits... \n")
    
        
    savings.deposit(500)
    checking.deposit(2000)

    print("after deposits")

    print("Savings balance: ",savings.balance)
    


    checking.transfer(savings,1000)

    print("Savings balance: ",savings.balance)
    print("Checking balance: ",checking.balance)


main()
