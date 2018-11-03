try :
    print("teste de try")
    print("Im "+30+"Years old")
except TypeError as t:
    print("Não se faz conversões implícitas de tipo ", str(t))
    log = str(t)
    saveLog = open("logDeErro.txt","w")
    saveLog.write(log)
    saveLog.close()    
except Exception as e:
    print("Deu ruim meu caro sabe porque ?  \n" + str(e))

print(5 + int("5"))



'''
try to catch specific errors

like
    except NameError as e  - related to variables that not exist and was used
    except TypeError as t
    except ValueError as v

    and so on
    
'''
