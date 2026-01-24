# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

isodd = lambda no : no%2!=0

def main():
      print("Enter number to returns True if number is odd otherwise False.")
      no = int(input())

      ans=isodd(no)
      
      print(ans)

if __name__ == "__main__":
        main()