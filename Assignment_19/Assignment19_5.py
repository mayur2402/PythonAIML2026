# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user.
#
# Filter:
#   Filter out all such numbers which are prime numbers.
#
# Map:
#   Multiply each filtered number by 2.
#
# Reduce:
#   Return the maximum number from the mapped list.
#   (You can use normal functions instead of lambda functions.)
#
# Input List:
#   [2, 70, 11, 10, 17, 23, 31, 77]
#
# List after filter:
#   [2, 11, 17, 23, 31]
#
# List after map:
#   [4, 22, 34, 46, 62]
#
# Output of reduce:
#   62


from functools import reduce



def ChkPrime(no):
    isprime = True
    if no == 2:
        return True
    for i in range(2,int(no/2)+1):
        if(no%i == 0):
            isprime = False
            break
    return isprime
    
def Multiply(no):
    return no*2

def product(lst,ans):
    if(lst> ans):
        return lst
    else:
        return ans
    
def main():
    print("How many elements")
    no = int(input())
    lst = []
    for i in range(no):
        print("Enter " + str(i + 1) + " number")
        element = int(input())
        lst.append(element)

    flst = list(filter(ChkPrime,lst))

    mlst = list(map(Multiply,flst))
    rans = 0
    ans = reduce(product,mlst,0)

    print(ans)

if __name__ == "__main__":
    main()