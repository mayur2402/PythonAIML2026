

import os
import sys


def main():
    if len(sys.argv) < 3:
        print("Invalid number of arguments")
        return
    
    dirName = sys.argv[1]
    extensionName = sys.argv[2]

    if not os.path.isdir(dirName):
        print("Invalid Directory Name")
        return
    lstFile = []
    for folderName, subFolderName, fileName in os.walk(dirName):
        
        for fName in fileName:
            extension = os.path.splitext(fName)
            extension = extension[len(extension)-1]

            if extension == extensionName:
                lstFile.append(fName)

if __name__ == "__main__":
    main()