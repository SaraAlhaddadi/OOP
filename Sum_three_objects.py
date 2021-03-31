# Prepared by : Shvm-k
# in this program I implement  the Sum of three objects operations 
# by __add__ and __radd__ (reverse add ) in my class

class Student:
    def __init__(self,a):
        self.average=a
    def __add__(self, other):
            return self.average + other.average
    def __radd__(self, other):
        return self.average+other

a=Student(10)
b=Student(5)
c=Student(7)
print("a+b+c",a+b+c) #a+b+c 22