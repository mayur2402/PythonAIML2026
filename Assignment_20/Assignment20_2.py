
import threading


def EvenFactor(no):
    ans = 0
    for i in range(2,no+1):
        if(no % i == 0):
           if(i % 2 == 0):
               ans =  ans + i
    print(ans)

def OddFactor(no):
    ans = 0
    for i in range(1,no+1):
        if(no % i == 0):
           if(i % 2 != 0):
               ans =  ans + i
    print(ans)


def main():
    t1 = threading.Thread(target=EvenFactor,args=(100,))
    t2 = threading.Thread(target=OddFactor,args=(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()