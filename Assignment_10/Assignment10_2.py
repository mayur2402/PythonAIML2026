#Write a program which accepts one number and prints sum of first N natural numbers.
#Input: 5
#Output: 15

def SumNaturalNUmber(No):
    sum = 0
    for i in range(No+1):
        sum = sum + i
    print(sum)

def main():
    print("Enter number to sum of natural numbers")
    No = int(input())
    SumNaturalNUmber(No)

if __name__ == "__main__":
    main()