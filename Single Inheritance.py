"""
    Inheritance
    -----------
    1)Single Inheritance
    2)Multiple Inheritance
    3)Multi Level Inheritance
    4)Hybrid Inheritance
    5)Hierarchical Inheritance
"""

class Addition:
    def add(self):
        a=int(input("Enter The A Value:"))
        b=int(input("Enter The B Value:"))
        c=a+b
        print("Addition:",c)

class Subtraction(Addition):
    def sub(self):
        a = int(input("Enter The A Value:"))
        b = int(input("Enter The B Value:"))
        c = a - b
        print("Subtraction:", c)

obj=Subtraction()
obj.add()
obj.sub()