#Write a program which accept one number and display below pattern.

#Input: 5
#Output:

#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5


def main():
    print("Enter number")
    no = int(input())

    for i in range(1,no+1,1):
        for j in range(1,no+1,1):
            if(i >= j):
                print(j,end="\t")
        print()

if __name__ == "__main__":
    main()