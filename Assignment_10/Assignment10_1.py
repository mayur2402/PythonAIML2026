#Write a program which accepts one number and prints multiplication table of that number.
#Input: 4
#Output:
#4 8 12 16 20 24 28 32 36 40

def MultiTable(No):
    for i in range(1,11):
        print(i*No , end="\t")

def main():
    print("Enter Number to prints multiplication table ")
    No = int(input())
    MultiTable(No)

if __name__ == "__main__":
    main()