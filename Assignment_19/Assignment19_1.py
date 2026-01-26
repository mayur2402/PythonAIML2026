#Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input: 4  Output: 16
#Input: 6  Output: 64

power = lambda no : no**2

def main():
    print("Enter number to show power of two")
    no = int(input())

    ans = power(no)

    print(ans)

if __name__ == "__main__":
    main()