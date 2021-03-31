# Prepared by : Shvm-k
# in this program I remake String class with implement for loop for this class
# this program find how many times a char repeated in a string
# the char and string are entered by user
class String:
    def __init__(self,s):
        self.string=s
    def __getitem__(self, item):
        return self.string[item]
    def __contains__(self, item):
        return item in self.string

def count_chr(string,chr):
    c=0
    for i in string:
        if  i in chr:
            c+=1
    return c

s=String(input("enter a string: "))
c=String(input("enter a character: "))
print(count_chr(s,c))