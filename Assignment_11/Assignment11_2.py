#Write a program which accepts one number and prints count of digits in that number.
#Input: 7521
#Output: 4

def Count(No):
    count = 0
    while(No > 0):
        No = int(No/10)
        count += 1
    print(count)

def main():
    print("Enter number to count of digits in that number")
    No = int(input())
    Count(No)
    
if __name__ == "__main__":
    main()