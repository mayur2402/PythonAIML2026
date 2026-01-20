#Write a program which accepts one number and prints that many numbers in reverse order.
#Input: 5
#Output: 5 4 3 2 1

def reversNumber(no):
    for i in range(no,0,-1):
        print(i, end="\t")

def main():
    print("Enter one number to prints that many numbers in reverse order")
    no = int(input())
    reversNumber(no)

if __name__ == "__main__":
    main()