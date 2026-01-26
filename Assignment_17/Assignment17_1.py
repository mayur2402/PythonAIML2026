"""Create a module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division.
All functions accept two parameters as number and perform the operation.
Write one python program which call all the functions from this module.
"""

from Arithmetic17_1 import *

def main():
    print("Enter First Number ")
    no1 = int(input())

    print("Enter Second Number ")
    no2 = int(input())

    ans = add(no1,no2)
    print("Addition is :", ans)

    ans = sub(no1,no2)
    print("Substraction is :", ans)

    ans = multi(no1,no2)
    print("Multiplication is :", ans)

    ans = div(no1,no2)
    print("Division is :", ans)

    
    
if __name__ == "__main__":
    main()
