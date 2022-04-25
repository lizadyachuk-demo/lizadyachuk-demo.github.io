from math import sqrt

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        s = self.a+self.b+self.c/2
        return sqrt(s * (s - self.a) * ( s - self.b) * (s - self.c))

    def is_valid(self):
        if self.a+self.b>=self.c and self.b+self.c>=self.a and self.c+self.a>=self.b:
            return True
        else:
            return False

    def is_right(self):
        if self.a**2+self.b**2==self.c**2:
            return True
        else:
            return False

t = Triangle(2,2,3)
print(t.perimeter())
print(t.area())
print(t.is_valid())
print(t.is_right())