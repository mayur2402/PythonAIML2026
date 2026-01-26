

import threading


def Prime(lst):
    for i in range(len(lst)):
        isprime = True
        for j in range(2,int(i/2) + 1):
            if(lst[i] % j == 0):
                isprime = False
                break
        if(isprime):
            print(lst[i], end="\t")


def NonPrime(lst):
    for i in range(len(lst)):
        isprime = True
        for j in range(2,int(i/2) + 1):
            if(lst[i] % j == 0):
                isprime = False
                break
        if(isprime == False):
            print(lst[i], end="\t")


def main():
    lst = [1,2,3,4,5,6,7,8,9,10]

    thread1 = threading.Thread(target=Prime,args=(lst,))
    thread2 = threading.Thread(target=NonPrime,args=(lst,))

    thread1.start()
    print()
    thread2.start()

    thread1.join()
    thread2.join()
    
if __name__ == "__main__":
    main()
