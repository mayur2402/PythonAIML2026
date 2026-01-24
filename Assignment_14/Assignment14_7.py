# Write a lambda function which accepts one number and returns True if divisible by 5.

isdivisiblebyfive = lambda no : no%5==0

def main():
      print("Enter number to returns True if divisible by 5")
      no = int(input())

      ans=isdivisiblebyfive(no)
      
      print(ans)

if __name__ == "__main__":
        main()