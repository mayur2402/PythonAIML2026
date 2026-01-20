#Write a program which accepts one number and prints that many numbers starting from 1.
#Input: 5
#Output: 1 2 3 4 5

def ShowNumber(No):
    for i in range(1,No+1):
        print(i, end="\t")

def main():
    print("Enter one number to prints that many numbers starting from 1")
    no = int(input())
    ShowNumber(no)

if __name__ == "__main__":
    main()