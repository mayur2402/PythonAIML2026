#Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input: 4 3  Output: 12
#Input: 6 3  Output: 18

multi = lambda no1,no2 : no1*no2

def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter second number")
    no2 = int(input())

    ans = multi(no1,no2)

    print(ans)

if __name__ == "__main__":
    main()