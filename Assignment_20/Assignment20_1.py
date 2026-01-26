
import threading


def Even():
    i = 10
    j = 2
    while(i != 0):
        print(j ,end="\t")
        j = j + 2
        i = i - 1
    print()

def Odd():
    i = 10
    j = 1
    while(i != 0):
        print(j ,end="\t")
        j = j + 2
        i = i - 1
    print()

def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()