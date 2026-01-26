

class Numbers:
    def __init__(self,no):
        self.value = no

    def checkPrime(self):
        half = int((self.value / 2) + 1)
        isprime = True
        for i in range(2,half):
            if(self.value % i == 0):
                isprime = False
                break

        return isprime

    def isPrefect(self):
        lst = []

        for i in range(1,int(self.value/2)+1):
            if(self.value%i == 0):
                lst.append(i)

        sum = 0
        for i in lst:
            sum += i

        if sum == self.value:
            return True
        else:
            return False

    def Factors(self):
        for i in range(1,int(self.value/2) + 1):
            if(int(self.value%i) == 0):
                print(i ,end="\t")
    
    def AdditionofFactorial(self):
        ans = 0

        for i in range(1,self.value+1):
            ans = ans +i

        return ans

print("Enter value")
value = int(input())


obj1 = Numbers(value)
isprime = obj1.checkPrime()
if(isprime):
    print("Prime Number")
else:
    print("Not prime")

isperfect = obj1.isPrefect()
if(isperfect):
    print("Perfect Number")
else:
    print("Not perfect number")

obj1.Factors()
print()
add = obj1.AdditionofFactorial()
print("Addition of factors is :", add)