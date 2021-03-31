# Prepared by : Shvm-k
# in this program I implement  the mathematical operations in my class

class M:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __add__(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
        self.c = self.c + other.c
        return self.a,self.b,self.c

    def __sub__(self, other):
        self.a = self.a - other.a
        self.b = self.b - other.b
        self.c = self.c - other.c
        return self.a,self.b,self.c

    def __mul__(self, other):
        self.a = self.a * other.a
        self.b = self.b * other.b
        self.c = self.c * other.c
        return self.a, self.b, self.c

    def __truediv__(self, other):
        self.a = self.a / other.a
        self.b = self.b / other.b
        self.c = self.c / other.c
        return self.a, self.b, self.c

    def __pow__(self, power, modulo=None):
        self.a = self.a ** power.a
        self.b = self.b ** power.b
        self.c = self.c ** power.c
        return self.a, self.b, self.c

    def __mod__(self, other):
        self.a = self.a % other.a
        self.b = self.b % other.b
        self.c = self.c % other.c
        return self.a, self.b, self.c

ob1 = M(2, 3, 5)
ob2 = M(8, 9, 1)
ob3 = M(7, 4, 1)
ob=M(2, 3, 5)
ob*ob2
print("ob1 * ob2 + ob3 = ",ob+ob3)

ob=M(2, 3, 5)
ob**ob2
print("ob1 ** ob2 - ob3 = ",ob-ob3)

ob=M(2, 3, 5)
ob/ob2
ob%ob3
ob*ob1
o=M(8, 9, 1)
o*ob3
print("ob1 / ob2 % ob3 * ob1 - ob2 * ob3 = ",ob-o)