#Write a program which accepts one number and checks whether it is divisible by 3 and 5.
#Input: 15
#Output: Divisible by 3 and 5

def Divibleby3and5(No):
    if(No % 3 == 0 and No % 5 == 0):
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
Divibleby3and5(15)
Divibleby3and5(20)