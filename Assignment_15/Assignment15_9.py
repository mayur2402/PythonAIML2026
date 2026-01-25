# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.


from functools import reduce


def Max(ans,no):
    ans = ans * no
    return ans

def main():
    print("How many numbers")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " number")
        i = int(input())

        lst.append(i)

    rlst = int(reduce(Max,lst))

    print(rlst)

if __name__ == "__main__":
    main()