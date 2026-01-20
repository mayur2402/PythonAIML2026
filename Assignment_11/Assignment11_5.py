#Write a program which accepts one number and checks whether it is palindrome or not.
#Input: 121
#Output: Palindrome
def Reverse(no):
    no1 = 0

    while(no != 0):
        rem = no%10
        no1 = no1*10 + rem
        no = int(no/10)
    return no1

def isPalindrome(no1,no2):
    if (no1 == no2):
        return True
    else:
        return False

def main():
    print("Enter number")
    no = int(input())
    ans = Reverse(no)
    ispal = isPalindrome(no,ans)
    if ispal:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()