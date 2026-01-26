import threading


def Sum(lst):
    sum = 0
    for i in lst:
        sum = sum + i

    print(sum)        


def Product(lst):
    sum = 1
    for i in lst:
        sum = sum * i

    print(sum)  

def main():
    lst = [1,2,3,4,5,6,7,8,9,10]

    thread1 = threading.Thread(target=Sum,args=(lst,))
    thread2 = threading.Thread(target=Product,args=(lst,))

    thread1.start()
    print()
    thread2.start()

    thread1.join()
    thread2.join()
    
if __name__ == "__main__":
    main()
