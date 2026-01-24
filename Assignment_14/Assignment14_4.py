#Write a lambda function which accepts two numbers and returns minimum number.

Max = lambda no1,no2 : no1>no2

def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter Second number")
    no2 = int(input())
    
    ans=Max(no1,no2)

    if(ans):
          print(no2 ,"is smaller")
    else:
          print(no1 ,"is smaller")

if __name__ == "__main__":
        main()