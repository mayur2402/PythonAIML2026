
import os


def main():
    print("Enter File Name")
    name = input()

    name = os.path.abspath(name)
    if(os.path.exists(name)):
        print("File exists")
    else:
        print("File doesn't exists")
        return

    obj = open(name,"r")

    print("Enter Name to search in file")
    stname = input()
    count = 0
    for line in obj:
        words = line.split()
        for word in words:

            if word.lower() == stname.lower():
                count = count + 1

    print(count)

if __name__ == "__main__":
    main()