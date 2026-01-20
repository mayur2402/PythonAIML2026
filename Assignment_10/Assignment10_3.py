#Write a program which accepts one number and prints factorial of that number.
#Input: 5
#Output: 120

def Factorial(No):
    fact = 1
    while(No > 0):
        fact = fact * No
        No -= 1
    return fact

def main():
    print("number to prints factorial of that number")
    No = int(input())
    ans = Factorial(No)
    print(ans)

if __name__ == "__main__":
    main()