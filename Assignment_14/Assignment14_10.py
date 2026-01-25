# Write a lambda function which accepts three numbers and returns largest number.

Max = lambda no1,no2,no3 : no1 if no1>no2 and no1 > no3 else ( no2 if no2 > no1 and no2> no3 else no3) 

def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter Second number")
    no2 = int(input())
    
    print("Enter third number")
    no3 = int(input())

    ans=Max(no1,no2,no3)

    print(ans)
if __name__ == "__main__":
        main()