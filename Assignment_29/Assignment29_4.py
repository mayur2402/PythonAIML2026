
import hashlib
import os
import sys

def hashfunc(obj1):
    hasher = hashlib.md5()

    data = obj1.read(1024)

    while(len(data) > 0):
        hasher.update(data)
        data = obj1.read(1024)

    return hasher.hexdigest()

def main():
    if(len(sys.argv) != 3):
        print("Provide correct arguments")
        return
    
    name1 = sys.argv[1]
    name2 = sys.argv[2]

    name1 = os.path.abspath(name1)
    if(os.path.exists(name1)):
        print("File exists")
    else:
        print("File doesn't exists")
        return

    name2 = os.path.abspath(name2)

    if(os.path.exists(name2)):
        print("File exists")
    else:
        print("File doesn't exists")
        return

    obj1 = open(name1,"rb")
    obj2 = open(name2,"rb")

    hasher1 = hashfunc(obj1)
    hasher2 = hashfunc(obj2)

    if(hasher1 == hasher2):
        print("Success")
    else:
        print("Failure")
    
if __name__ == "__main__":
    main()