#Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
#Input:
#Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5

#Output: 3

def Frequency(lst,no):
    count = 0
    for i in lst:
        if(i == no):
            count = count + 1

    return count

def main():
    print("How many number of elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i+1) + " element")
        element = int(input())
        lst.append(element)
    print("Enter number to check frequency of that number from List")
    no = int(input())
    ans = Frequency(lst,no)

    print(ans)

if __name__ == "__main__":
    main()