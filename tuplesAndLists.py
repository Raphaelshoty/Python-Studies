def function():
    return 28,29,30 # this is a tuple like (28,29,30) and its immutable

a, b, c = function()

print(a)
print(b)
print(c)

tup = (1,2,3,4,5,6,7,8,9,10)
print(tup[3])


'''
now list and list operations
'''

lst = [1,2,3,4,5,6]

print(lst[5])

lst.append(7)

print(lst)

lst.insert(0,0)

print(lst)

lst.remove(2) # if we have multiple elements that matches with this pattern only the first one will be removed
print(lst)



lst.pop()

print(lst)

print(lst.index(5))


lst.sort()
print(lst)
lst.reverse()
print(lst)
