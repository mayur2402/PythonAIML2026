# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

def odd(no):
    return no%2 != 0

def main():
    print("How many numbers")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " Number")
        i = int(input())

        lst.append(i)

    rlst = list(filter(odd,lst))

    print(rlst)

if __name__ == "__main__":
    main()