##class Employee:
##    pass
##
##    def __init__(self, firstName, lastName, age):
##        self.__firstName = firstName
##        self.__lastName = lastName
##        self.__age = age
##
##    def getFirstName(self):
##        return self.__firstName
##
##    def getLastName(self):
##        return self.__lastName
##
##    def getAge(self):
##        return self.__age
##
##    
##    
##def main():
##    pessoa = Employee("Candango","Qualquer",22)
##
##    print("Employee First Name: {}".format(pessoa.getFirstName()))
##    print("Employee Last Name: {}".format(pessoa.getLastName()))
##    print("Employee Age: {}".format(pessoa.getAge()))
##
##main()


class Pessoa:
    pass

    firstName = None
    lastName  = None
    age = None

    def __init__(self, firstName , lastName ,  age ):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getAge(self):
        return self.age
    def getLastName(self):
        return self.lastName
    def getFirstName(self):
        return self.firstName

    def setAge(self,age):
        self.age = age
    def setLastName(self, lastName):
        self.lastName = lastName
    def setFirstName(self, firstName):
        self.firstName = firstName

def main():
    print("First name: ",Pessoa.firstName)#class attr
    print("Last name: ",Pessoa.lastName)#class attr
    print("Age: ",Pessoa.age)#class attr

    print("-------- changes------------")
    pelego = Pessoa("","", 0)

    pelego.setFirstName("Pelego")
    pelego.setLastName("Doidão")
    pelego.setAge(20)

    print("Pelego's age : ",pelego.getAge())
    print("Pelego's First Name: ",pelego.getFirstName())
    print("Pelego's Last Name: ", pelego.getLastName())
    

main()
