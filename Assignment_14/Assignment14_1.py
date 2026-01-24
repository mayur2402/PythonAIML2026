#Write a lambda function which accepts one number and returns square of that number.

Square = lambda no : no*no

def main():
    print("Enter one number to returns square of that number")
    no = int(input())

    ans=Square(no)

    print("Square of number is : " , ans)

if __name__ == "__main__":
        main()