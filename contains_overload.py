# Prepared by : Shvm-k
# in this program I implement  the __contains__ operations in my class

class Student:
    def __init__(self,l):
        self.marks=l
    def __contains__(self, item):
        for i in self.marks:
            if i==item:
                return True
        else:
            return False

a=Student([1,2,3])
b=Student([4,5])
print("20 in a",20 in a)
print("4 in b",4 in b)