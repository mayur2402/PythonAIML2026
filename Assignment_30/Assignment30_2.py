import os


def main():
    print("Enter File Name")
    name = input()

    name = os.path.abspath(name)

    if not (os.path.exists(name)):
        print("Incorrect file Name")

    fobj = open(name,"r")

    count = 0
    for line in fobj:
        words = line.split()
        for word in words:
            count = count + 1

    print(count)

if __name__ == "__main__":
    main()