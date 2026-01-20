#Write a program which accepts one number and prints binary equivalent.
def Binary(no):
    lst = []
    while(no > 0):
        rem = int(no%2)
        no = int(no/2)
        lst.append(rem)

    bin = ''
    for i in range(len(lst)-1,-1,-1):
        bin = bin + str(lst[i])

    print(bin)

def main():
    print("Enter number to prints binary equivalent")
    no = int(input())
    Binary(no)


if __name__ == "__main__":
    main()