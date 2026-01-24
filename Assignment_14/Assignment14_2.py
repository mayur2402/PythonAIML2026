#Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda no : no*no*no

def main():
    print("Enter one number to returns cube of that number")
    no = int(input())

    ans=Cube(no)

    print("Cube of number is : " , ans)

if __name__ == "__main__":
        main()