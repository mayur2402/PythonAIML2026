

import threading


def Max(lst):
    max = lst[0]
    for i in range(2,len(lst)):
        if(max < lst[i]):
            max = lst[i]

    print(max)        


def Min(lst):
    min = lst[0]
    for i in range(2,len(lst)):
        if(min > lst[i]):
            min = lst[i]

    print(min) 

def main():
    lst = [1,2,3,4,5,6,7,8,9,10]

    thread1 = threading.Thread(target=Max,args=(lst,))
    thread2 = threading.Thread(target=Min,args=(lst,))

    thread1.start()
    print()
    thread2.start()

    thread1.join()
    thread2.join()
    
if __name__ == "__main__":
    main()
