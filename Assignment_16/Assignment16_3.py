#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
#Input: 11 5
#Output: 16


def Addition(No1,No2):
    ans = No1+No2
    print("Addition is :", ans)

def main():
    print("Enter First Number ")
    no1 = int(input())
    print("Enter Second Number ")
    no2 = int(input())

    Addition(no1,no2)

if __name__ == "__main__":
    main()