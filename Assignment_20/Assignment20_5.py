import threading

lock = threading.Lock()

def Thread1():
    lock.acquire()
    for i in range(1, 51):
        print(i, end=" ")
    print()
    lock.release()

def Thread2():
    lock.acquire()
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()
    lock.release()

def main():
    t1 = threading.Thread(target=Thread1, name="Thread1")
    t2 = threading.Thread(target=Thread2, name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
