#Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
#Input:
#Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34

Output: 56

def Maximum(lst):
    max = 0
    for i in lst:
        if(i > max):
            max = i

    return max

def main():
    print("How many number of elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i+1) + " element")
        element = int(input())
        lst.append(element)

    ans = Maximum(lst)

    print(ans)

if __name__ == "__main__":
    main()