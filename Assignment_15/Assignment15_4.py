# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce


def Add(ans,no):
    ans = ans + no
    return ans

def main():
    print("How many numbers")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " Number")
        i = int(input())

        lst.append(i)

    rlst = int(reduce(Add,lst))

    print(rlst)

if __name__ == "__main__":
    main()