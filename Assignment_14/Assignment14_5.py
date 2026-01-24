# Write a lambda function which accepts one number and returns True if number is even otherwise False.

iseven = lambda no : no%2==0

def main():
      print("Enter number to returns True if number is even otherwise False")
      no = int(input())

      ans=iseven(no)
      
      print(ans)

if __name__ == "__main__":
        main()