# Write a lambda function which accepts two numbers and returns addition.

multi = lambda no1,no2 : no1*no2

def main():
      print("Enter first number")
      no1 = int(input())

      print("Enter first number")
      no2 = int(input())

      ans=multi(no1,no2)
      
      print(ans)

if __name__ == "__main__":
        main()