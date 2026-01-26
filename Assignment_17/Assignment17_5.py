#Write a program which accept one number from user and check whether number is prime or not.
#Input: 11
#Output: It is Prime Number



def isprime(no):
    prime = False
    for i in range(2,int(no/2)+1):
        if (no % i == 0):
            prime = True
    return prime

def main():
    print("Enter Number to returns to check whether number is prime or not")
    no = int(input())
    ans = isprime(no)
    if(ans):
        print("It is not Prime Number")
    else:
        print("It is Prime Number")

if __name__ == "__main__":
    main()