# Prepared by : Shvm-k
# in this program I implement  the __len__ operations in my class

class Student:
    def __init__(self,l):
        self.marks=l
    def __len__(self):
        return len(self.marks)

a=Student([1,2,3])
b=Student([4,5])

print("len(a)",len(a))
print("len(a)==len(b)",len(a)==len(b))
