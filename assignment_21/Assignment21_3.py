import threading
count = 0
lock = threading.Lock()

def increament():
    global count

    for i in range(1000):
        lock.acquire()
        count = count + i
        lock.release()

    print(count)

def main():
    lst = [1,2,3,4,5,6,7,8,9,10]

    thread1 = threading.Thread(target=increament)
    thread2 = threading.Thread(target=increament)

    thread1.start()
    print()
    thread2.start()

    thread1.join()
    thread2.join()
    
if __name__ == "__main__":
    main()
