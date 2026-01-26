# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
#
# Filter:
#   Filter out all such numbers which are even.
#
# Map:
#   Calculate the square of each filtered number.
#
# Reduce:
#   Return the addition (sum) of all numbers obtained after map operation.
#
# Input List:
#   [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#
# List after filter:
#   [2, 4, 4, 2, 8, 10]
#
# List after map:
#   [4, 16, 16, 4, 64, 100]
#
# Output of reduce:
#   204


from functools import reduce


def even(no):
    if no % 2 == 0:
        return True
    else:
        return False
    
def square(no):
    return no**2

def product(lst,ans):
    return ans + lst
    
def main():
    print("How many elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i + 1) + " number")
        element = int(input())
        lst.append(element)

    flst = list(filter(even,lst))

    mlst = list(map(square,flst))
    rans = 0
    ans = reduce(product,mlst,0)

    print(ans)

if __name__ == "__main__":
    main()