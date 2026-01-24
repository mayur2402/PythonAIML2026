# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.


from functools import reduce

def even(no):
    if no%2 == 0:
        return True

def Max(ans,no):
    ans = ans + 1
    return ans

def main():
    print("How many numbers")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " number")
        i = int(input())

        lst.append(i)

    elst = list(filter(even,lst))

    print(len(elst))

if __name__ == "__main__":
    main()