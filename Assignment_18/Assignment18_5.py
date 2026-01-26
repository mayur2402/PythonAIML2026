# Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to
# ChkPrime() function which is part of our user defined module named as MarvellousNum.
# Name of the function from main python file should be ListPrime().
#
# Input:
# Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#
# Output: 32 (13 + 5 + 7 + 2 + 5)

from MarvellousNum import ChkPrime

def  ListPrime(lst,no):
    ans = 0
    for i in lst:
        isprime = ChkPrime(i)
        if(isprime):
            ans = ans + i

    return ans

def main():
    print("How many number of elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i+1) + " element")
        element = int(input())
        lst.append(element)


    ans =  ListPrime(lst,no)

    print(ans)

if __name__ == "__main__":
    main()