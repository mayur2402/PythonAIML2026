
import os


def main():
    print("Enter file name")
    name = input()

    name = os.path.abspath(name)
    print(name)
    if(os.path.exists(name)):
        print("File exists")
    else:
        print("File doesn't exists")

if __name__ == "__main__":
    main()