#Write a program which accepts one number and prints its factors.
#Input: 12
#Output: 1 2 3 4 6 12

def Factors(no):
    for i in range(1,int(no/2) + 1):
        if(int(no%i) == 0):
            print(i ,end="\t")
    print(no)

def main():
    print("Enter one number to prints its factors")
    no = int(input())
    Factors(no)

if __name__ == "__main__":
    main()