#Write a program which accepts one number and prints reverse of that number.
#Input: 123
#Output: 321

def Reverse(No):
    count = 0
    while(No > 0):
        ret = int(No%10)
        No = int(No/10)
        count += ret
    print(count)

def main():
    print("Enter number to sum of digits in that number")
    No = int(input())
    Reverse(No)
    
if __name__ == "__main__":
    main()