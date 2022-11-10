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
class A:
    def __init__(self,v):
        self.a=v+2

a=A(0)
print(a.a)

        