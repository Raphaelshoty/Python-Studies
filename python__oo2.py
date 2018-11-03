#### __propertie  -> private
#### _propertie -> protected
#### propertie -> public

class Veiculo:
    pass
# this way of declargin the constructor or the initializer can take the attributes directly as parameters
#this way you have to pass the parameters to be set on the attributes
    def __init__(self, tipo, ano, modelo):
        self.__tipo = tipo # that way the propertie or the attribute is private
        self.__ano = ano
        self__modelo = modelo

    def setTipo(self,tipo):
        self.__tipo = tipo
        
    def getTipo(self):
        return self.__tipo

    def setAno(self, ano):
        self.__ano = ano

    def getAno(self):
        return self.__ano

    def setModelo(self, modelo):
        self.__modelo = modelo

class Professor:
    pass
#This way the initializer can set the attributes directly inside the __init__
#this way the objetc starts its life accepting pre set values into its attributes
    def __init__(self, subject = None, name = None):
        self.__subject = subject
        self.__name = name

    def setSubject(self, subject):
        self.__subject = subject
        
    def setName(self, name):
        self.__name = name
        
    def getSubject(self):
        return self.__subject
    
    def getName(self):
        return self.__name
        

def main():
    carro = Veiculo("carro",2012,"Corola")
    setattr(carro,'__cor',"verde")
    print(getattr(carro,'__cor'))
    print(hasattr(carro,'__cor'))
    print(type(carro.getTipo()))

main()
        
