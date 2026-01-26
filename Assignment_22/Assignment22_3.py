
class Arithematic:

    def __init__(self):
         self.value1 = 0.0
         self.value2 = 0.0

    def Accept(self):
        print("Enter value 1")
        self.value1 = float(input())
        print("Enter value 2")
        self.value2 = float(input())

    def Addition(self):
        return self.value1 + self.value2

    def Substraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        return self.value1 / self.value2

def main():
    obj1 = Arithematic()
    obj1.Accept()
    add = obj1.Addition()
    print("Addition is : ", add)
    sub = obj1.Substraction()
    print("Substraction is : ", sub)
    mul = obj1.Multiplication()
    print("Multiplication is : ", mul)
    div = obj1.Division()
    print("Division is : ", div)

if __name__ == "__main__":
    main()