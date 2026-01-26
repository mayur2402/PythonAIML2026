# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
#
# Filter:
#   Filter out all such numbers which are greater than or equal to 70
#   and less than or equal to 90.
#
# Map:
#   Increase each filtered number by 10.
#
# Reduce:
#   Return the product of all numbers obtained after map operation.
#
# Input List:
#   [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#
# List after filter:
#   [76, 89, 86, 90, 70]
#
# List after map:
#   [86, 99, 96, 100, 80]
#
# Output of reduce:
#   6538752000

from functools import reduce


def greaterthan70lessthan90(no):
    if no > 70 and no < 90:
        return True
    else:
        return False
    
def IncreaseBy10(no):
    return no+10

def product(lst,ans):
    return ans * lst
    
def main():
    print("How many elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i + 1) + " number")
        element = int(input())
        lst.append(element)

    flst = list(filter(greaterthan70lessthan90,lst))

    mlst = list(map(IncreaseBy10,flst))
    rans = 0
    ans = reduce(product,mlst,1)

    print(ans)

if __name__ == "__main__":
    main()