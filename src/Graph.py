from Aspect import Aspect
from Item import Item

ldc = Aspect('a3')  # Leonardo di Caprio
th = Aspect('a1')   # Tom Hanks
ss = Aspect('d1')   # Steven Spielberg
b = Aspect('g2')    # biography
d = Aspect('g3')    # drama

cmic = Item('f1',[ldc,th,ss,b,d])   # Catch me if you can

# add users rating to item
cmic.add_user('Bob', 4, 4.5,4)
cmic.add_user('Alice', 4.5, 4.5,4.5)
cmic.add_user('John', 4,4,4)

# add users rating to all aspects
ldc.add_user('Bob', 4.2, 4.5,4.2)
ldc.add_user('Alice', 4.1, 4.5,4.1)
ldc.add_user('John', 3.9,4,3.9)
th.add_user('Bob', 4.2, 4.5,4.2)
th.add_user('Alice', 4.5, 4.5,4.5)
th.add_user('John', 4,4,4)
ss.add_user('Bob', 4, 4.5,4)
ss.add_user('Alice', 4.7, 4.5,4.7)
ss.add_user('John', 4.2,4,4.2)
b.add_user('Bob', 4, 4.5,4)
b.add_user('Alice', 4.5, 4.5,4.5)
b.add_user('John', 4.3,4,4.3)
d.add_user('Bob', 4, 4.5,4)
d.add_user('Alice', 2.5, 4.5, 2.5)
d.add_user('John', 4,4,4)

print(cmic.predicted_rating)
print(d.predicted_rating)