# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.


def Max(string):
    if len(string) > 5:
        return string

def main():
    print("How many strings")
    no = int(input())

    lst = list()

    for i in range(no):
        print("Enter ", i+1 , " String")
        i = input()

        lst.append(i)

    rlst = list(filter(Max,lst))

    print(rlst)

if __name__ == "__main__":
    main()