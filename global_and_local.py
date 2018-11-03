x  = 7 

'''
def func1():
  global x 
  x +=1
  print(x)

func1()
print(x)


this above is considered bad practice
'''
print(x)

def func2():  
  y = x + 1 # so y is equal to 8
  return y

x = func2()
print(x)

# the example above is considered best practice in assigning new values to a global
# variable
