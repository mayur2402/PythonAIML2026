#Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#Input:
#Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output: 130

def Addition(lst):
    ans = 0
    for i in lst:
        ans = ans + i

    return ans

def main():
    print("How many number of elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i+1) + " element")
        element = int(input())
        lst.append(element)

    ans = Addition(lst)

    print(ans)

if __name__ == "__main__":
    main()