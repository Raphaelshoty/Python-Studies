class Pessoa:
    pass
    firstName = ''
    lastName = ''
    
    def __init__(self,firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @firstName.setter
    def firstName(self,firstName):
        if(not isinstance(firstName, str)):
            raise TypeError("Assign just text")
        elif(firstName  == None or firstName == ''):
            raise ValueError("Cannot assign empty value")
        else:
            self.__firstName = firstName

    def setFirstName(self,firstName):
        self.firstName = firstName

    @lastName.setter
    def lastName(self,lastName):
        if(not isinstance(lastName, str)):
            raise TypeError("Assign just text")
        elif(lastName  == None or lastName == ''):
            raise ValueError("Cannot assign empty value")
        else:
            self.__lastName = lastName

    def setLastName(self,lastName):
        self.lastName = lastName

#-----------------------------------------------------------

class Account:
    pass

    number = 0
    balance = 0
    owner = Pessoa("owner","ownerLastName")
    limitCred = 1000
    
    def __init__(self,number,balance,Pessoa):
        self.__number = number
        self.__balance = balance
        self.__owner = Pessoa

    @property
    def number(self):
        return self.__number

    @property
    def balance(self):
        return self.__balance

    @number.setter
    def number(self,number):
        if(not isinstance(number, int)):
            raise TypeError("cannot assign a non numeric value")
        elif(number < 0):
            raise ValueError("cannot assign negative values to number account")
        else:
            self.__number = number

    def setNumber(self, number):
        self.number = number        
    
    @balance.setter
    def balance(self, balance):
        if(not isinstance(balance, int) or not isinstance(balance, float)):
            raise TypeError("Cannot assign a non numeric value")
        else:
            self.__balance = balance

    def setBalance(self,balance):
        self.balance = b

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        if( not isinstance(owner,Pessoa)):
            raise TypeError("The Owner has to be an Pessoa")
        else:
            self.__owner = owner

    def setOwner(self, owner):
        self.owner = owner

    def getDetails(self):
        print("Account owner: " + getattr(self,'owner').firstName + " "+getattr(self,'owner').lastName)
        print("Account Number: ", self.number)
        print("Account Balance: ", self.balance)

    def withdraw(self, ammount):
        if(balance + limitCred  > ammount ):
            setBalance((balance + limitCred) - ammount)
        else:
            raise ValueError("There's no enoght funds for that operation")
              
    def deposit(self, ammount):
        setBalance(balance + ammount)
        

    
def main():
    conta = Account(1,5000,Pessoa("Raphael","Lima"))
    conta.getDetails()
    conta2 = Account(2,10000000000000, Pessoa("Bill","Gates"))
    conta2.getDetails()   

   

main()
