class Pessoa:
    pass

    def __init__(self, name, age, height, weight ):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight    
        
    @property
    def name(self):
        return self.__name    

    @name.setter
    def name(self,name):
        if(name == None  ):
            raise ValueError("Cannot assign an empty value!")            
        else:
            self.__name = name
    
    
    def setName(self, name):
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if(age < 0 or False == isinstance(age, int)):
            raise ValueError(" age less than 0 or age is not a number ")
        else:
            self.__age = age

    def setAge(self, age):
        self.__age = age
      
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if(not isinstance(height,float)):
            raise TypeError("Height must be like 1.82")
        elif(height < 0):
            raise ValueError("You cant assign negative values")
        else:
            self.__height = height

    def setHeight(self, height):
        self.height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,weight):
        if(weight < 0):
            raise ValueError("cant assign negative weight")
        else:
            self.__weight = weight

    def setWeight(self, weight):
        self.weight = weight
   
def main():
    fulano = Pessoa("fulano",25,1.75,76)
    fulano.setHeight(1.85)
    fulano.setWeight(76)
    print(fulano.weight)
    print(fulano.height)
    
main()

