
class Circle:
    PI = 3.14

    def __init__(self):
         self.radius = 0.0
         self.area = 0.0
         self.cir = 0.0

    def Accept(self):
        print("Enter radius of circle")
        self.radius = float(input())

    def CalculateArea(self):
        self.area = Circle.PI * self.radius**2

    def CalculateCircumference(self):
        self.cir = 2*Circle.PI*self.radius

    def Display(self):
        print("Radius of Circle is : ", self.radius)
        print("Area of Circle is : ", self.area)
        print("Circumference of circle is : ", self.cir)

def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__ == "__main__":
    main()