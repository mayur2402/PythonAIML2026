#Write a program which accepts one number and checks whether it is prime or not.
#Input: 11
#Output: Prime Number

def checkPrime(No):
    half = int((No / 2) + 1)
    isprime = True
    for i in range(2,half):
        if(No % i == 0):
            isprime = False
            break

    return isprime

def main():
    print("Enter number to checks whether it is prime or not")
    No = int(input())
    isprime = checkPrime(No)
    if(isprime):
        print("Prime")
    else:
        print("Not Prime")

if __name__ == "__main__":
    main()