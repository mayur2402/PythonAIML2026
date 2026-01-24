# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.


def Max(no):
    if no%3 == 0 and no%5 == 0:
        return no

def main():
    print("How many numbers")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " number")
        i = int(input())

        lst.append(i)

    rlst = list(filter(Max,lst))

    print(rlst)

if __name__ == "__main__":
    main()