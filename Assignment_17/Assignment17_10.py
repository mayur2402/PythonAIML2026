#Write a program which accept number from user and return addition of digits in that number.
#Input: 5187934
#Output: 37

def NoOfDigit(no):
    ans = 0
    while(no != 0):
        rem = no % 10
        no = int(no / 10)
        ans = ans + rem

    return ans

def main():
    print("Enter number to retrun addition of digits in that number.")
    no = int(input())
    ans = NoOfDigit(no)
    print(ans)


if __name__ == "__main__":
    main()