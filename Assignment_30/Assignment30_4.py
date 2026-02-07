
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

    print("Enter file name where you want to copy content")
    outputfile = input()
    oobj = open(outputfile,"w")
    for line in content:
        oobj.write(line)

if __name__ == "__main__":
    main()