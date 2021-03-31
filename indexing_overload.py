# Prepared by : Shvm-k
# in this program I implement  the index []  operations by __getitem__ in my class

class Student:
    def __init__(self,l):
        self.marks=l
    def __getitem__(self, item):
        return self.marks[item]

a=Student([1,2,3])
b=Student([4,5])
for i in a:
    print(i)

print("a[0]",a[0])
print("b[:2]",b[:2])
print("b[-1]",b[-1])