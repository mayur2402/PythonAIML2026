#3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def multi(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1/no2

def main():
    print("Enter First Number")
    no1 = int(input())
    print("Enter Second Number")
    no2 = int(input())

    addans = add(no1,no2)
    print("Addition is : ", addans)

    subans = sub(no1,no2)
    print("Substraction is : ", subans)
          
    multians = multi(no1,no2)
    print("Multiplication is : ", multians)
          
    divans = div(no1,no2)
    print("Division is : ", divans)


if __name__ == "__main__":
    main()