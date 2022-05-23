import math
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=(input("Enter the operator: +, -, *, / : "))
if c == '+':
    print(a+b)
elif c == "-":
    print(a-b) 
elif c == '*':
    print(a*b)
elif c== "/":
    print(a/b)
else:
    print("Invalid operator")       
