#Write a program which accept number from user and return number of digits in that number.

#Input: 5187934
#Output: 7

def NoOfDigit(no):
    count = 0
    while(no != 0):
        rem = no % 10
        no = int(no / 10)
        count = count + 1

    return count

def main():
    print("Enter number to retrun number of digits in that number.")
    no = int(input())
    ans = NoOfDigit(no)
    print(ans)


if __name__ == "__main__":
    main()