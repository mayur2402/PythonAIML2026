#Write a program which accept one number from user and returns its factorial.
#Input: 5
#Output: 120

def Factorial(no):
    ans = 1

    for i in range(1,no+1):
        ans = ans *i

    return ans

def main():
    print("Enter Number to returns its factorial")
    no = int(input())
    ans = Factorial(no)
    print(ans)

if __name__ == "__main__":
    main()