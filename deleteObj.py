import time as t

class Pessoa:
    pass

    def __init__(self):
        t.sleep(3)
        print("Objeto criado")

    def __del__(self):
        t.sleep(3)
        print("Objeto destruído")
        


def main():
    obj = Pessoa()
    obj2 = Pessoa()
    
    del(obj)
    del(obj2)

main()
