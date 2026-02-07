
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

    content = obj.read()

    print(content)

if __name__ == "__main__":
    main()