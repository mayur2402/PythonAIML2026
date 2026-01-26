
#Write a program which accept one number from user and return addition of its factors.
#Input: 12
#Output: 16



def AdditionofFactorial(no):
    ans = 0

    for i in range(1,no+1):
        ans = ans +i

    return ans

def main():
    print("Enter Number to returns its factorial")
    no = int(input())
    ans = AdditionofFactorial(no)
    print(ans)

if __name__ == "__main__":
    main()