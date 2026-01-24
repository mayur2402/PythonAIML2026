#Write a lambda function which accepts two numbers and returns maximum number.

Max = lambda no1,no2 : no1>no2

def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter Second number")
    no2 = int(input())
    
    ans=Max(no1,no2)

    if(ans):
          print(no1 ,"is greater")
    else:
          print(no2 ,"is greater")

if __name__ == "__main__":
        main()