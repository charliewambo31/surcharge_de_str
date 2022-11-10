"""class A:
    def __str__(self):
        return "a"

class B:
    def __str__(self):
        return "b"

class C(A,B):
        pass

o=C()
print(o)"""
"""class A:
    def __init__(self,v):
        self.a=v+2

a=A(0)
print(a.a)"""

import random
x = [1,2,3,4,5]
random.shuffle(x)
print(x)
##################################
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
########################################################
import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")
###################################
retourne absent car nous supposons que le fichier n existe pas 


        