class food:

    # Constructor
     def __init__(self, n1, col):
       self.name = n1
       self.color = col
# Object Creation
ob1 = food('pizza', 'cheese')
ob2 = food('momo', 'steam')
ob3 = food('fries','small')
# Calling Function
print(ob1.name)
print(ob1.color)
print(ob2.name)
print(ob2.color)
print(ob3.name)
print(ob3.color)