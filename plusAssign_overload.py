# Prepared by : Shvm-k
# in this program I implement the += operations 

class Student:
    def __init__(self,a):
        self.average=a
    def __iadd__(self, other):
        if type(other)==int:
            return self.__class__(self.average+other)
        else:
            return self.__class__(self.average + other.average)
    def __str__(self):
        return str(self.average)

a=Student(10)
b=Student(5)
a+=10
print("a+=10",a)
b+=a
print("b+=a",b)