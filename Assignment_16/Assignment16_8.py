#Write a program which accept number from user and print that number of "*" on screen.
#Input: 5
#Output: * * * * *



def main():
    
    print("Enter Number")
    no = int(input())
    for i in range(no):
        print("*",end="\t")
    
if __name__ == "__main__":
    main()