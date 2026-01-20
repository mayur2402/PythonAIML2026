#Write a program which accepts one number and prints all odd numbers till that number.

def oddNumber(No):
    for i in range(1,No+1):
        if(i % 2 != 0):
            print(i)

    
def main():
    print("Enter number to prints all even numbers till that number")
    no = int(input())
    oddNumber(no)

if __name__ == "__main__":
    main()