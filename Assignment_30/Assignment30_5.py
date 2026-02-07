import os


def main():
    print("Enter File Name")
    name = input()

    name = os.path.abspath(name)

    if not (os.path.exists(name)):
        print("Incorrect file Name")

    fobj = open(name,"r")

    print("Enter Word to search in file")
    stname = input()
    isfound = False
    for line in fobj:
        words = line.split()
        for word in words:
            if word.lower() == stname.lower():
                isfound = True
                break
        if isfound:
            break

    if isfound:
        print("Word found in file")
    else:
        print("Word is not in file")

if __name__ == "__main__":
    main()