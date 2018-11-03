class Pessoa:
    'the base of the class'

    firstName = 'John' # class attribute
    lastName = 'Doe' # class attribute
    age = 30    # class attribute
    
    #initializer of the class as known as constructor
    def __init__(self):
        self.firstName = '' # object attribute
        self.lastName = '' # object attribute
        self.__age = 0 # object attribute
        #declare some attributes

    def setFirstName(self,firstName):
        self.firstName = firstName
        
    def setLastName (self,lastName):
        self.lastName = lastName
        
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def setAge(self,age):
        self.age = age

    def getAge(self):
        return self.age

##eu = Pessoa()
##eu.setFirstName("Raphael")
##eu.setLastName("Lima")
##eu.setAge(30)
##print(eu.getFirstName() +" "+ eu.getLastName())
##
##print(eu.getAge())

