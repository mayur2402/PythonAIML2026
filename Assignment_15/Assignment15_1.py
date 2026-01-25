#Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

def square(no):
    return no*no

def main():
    print("How many numbers")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " Number")
        i = int(input())

        lst.append(i)

    rlst = list(map(square,lst))

    print(rlst)

if __name__ == "__main__":
    main()