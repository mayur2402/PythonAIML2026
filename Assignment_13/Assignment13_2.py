#Write a program which accepts length and width of rectangle and prints area.

PI = 3.14
def AreaOfCircle(radius):
    return PI*radius*radius

def main():
    print("Enter Radius of Circle")
    radius = float(input())

    area = AreaOfCircle(radius)

    print("Area of Circle is : ", area)
if __name__ == "__main__":
    main()