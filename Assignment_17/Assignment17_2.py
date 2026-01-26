#Write a program which accept one number and display below pattern.
#Input: 5
#Output:

#* * * * *
#* * * *
#* * *
#* *
#*

def main():
    print("Enter number")
    no = int(input())

    for i in range(no,0,-1):
        for j in range(i,0,-1):
            if(j <= i):
                print("*",end="\t")
        print()

if __name__ == "__main__":
    main()