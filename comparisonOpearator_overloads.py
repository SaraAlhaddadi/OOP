# Prepared by : Shvm-k
# in this program I implement the comparison operations in my class

class Student:
    def __init__(self,a):
        self.average=a
    
    # operation ==
    def __eq__(self, other):
        if type(other)==int:
            return self.average==other
        else:
            return self.average == other.average
    # operation !=
    def __ne__(self, other):
        if type(other)==int:
            return self.average!=other
        else:
            return self.average != other.average
    # operation >
    def __gt__(self, other):
        if type(other)==int:
            return self.average>other
        else:
            return self.average > other.average
    # operation >=
    def __ge__(self, other):
        if type(other)==int:
            return self.average>=other
        else:
            return self.average >= other.average
    # operation <
    def __lt__(self, other):
        if type(other)==int:
            return self.average<other
        else:
            return self.average < other.average
    # operation <=
    def __le__(self, other):
        if type(other)==int:
            return self.average<=other
        else:
            return self.average <= other.average

a=Student(10)
b=Student(5)

print("a==1",a==1)
print("a==b",a==b) 
print("5==b",5==b)

print("a!=1",a!=1)
print("a!=b",a!=b)
print("5!=b",5!=b)

print("a>1",a>1)
print("a>b",a>b)

print("a>=1",a>=1)
print("a>=b",a>=b)

print("a<1",a<1)
print("a<b",a<b)

print("a<=10",a<=10)
print("a<=b",a<=b)