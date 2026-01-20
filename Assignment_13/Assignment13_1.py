#Write a program which accepts length and width of rectangle and prints area.


def AreaOfRectangle(length,width):
    return length*width

def main():
    print("Enter length of rectangle")
    length = float(input())
    print("Enter width of rectangle")
    width = float(input())
    area = AreaOfRectangle(length,width)

    print("Area of rectangle is : ", area)
if __name__ == "__main__":
    main()