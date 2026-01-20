#Write a program which accepts one number and checks whether it is perfect number or not.
#Input: 6
#Output: Perfect Number

def isPrefect(no):
    lst = []

    for i in range(1,int(no/2)+1):
        if(no%i == 0):
            lst.append(i)

    sum = 0
    for i in lst:
        sum += i

    if sum == no:
        return True
    else:
        return False

def main():
    print("Enter number to checks whether it is perfect number or not")
    no = int(input())
    isperfect = isPrefect(no)
    if(isperfect):
        print("Perfect number")
    else:
        print("Not Perfect Number")


if __name__ == "__main__":
    main()