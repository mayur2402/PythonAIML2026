
import threading


def small(s):
    count = 0
    for i in range(len(s)):
        if s[i] >= str('a') and s[i] <= str('z'):
            count = count + 1
    print(count)
    print(threading.current_thread()) 

def capital(s):
    count = 0
    for i in range(len(s)):
        if s[i] >= str('A') and s[i] <= str('Z'):
            count = count + 1
    print(count)
    print(threading.current_thread()) 

def digit(s):
    count = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            count = count + 1
    print(count)
    print(threading.current_thread()) 

def main():
    t1 = threading.Thread(target=small,args=("Marvellous71",))
    t2 = threading.Thread(target=capital,args=("Marvellous71",))
    t3 = threading.Thread(target=digit,args=("Marvellous71",))

    print(id(t1))
    print(id(t1))
    print(id(t1))

    print()

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("Exit from main")

if __name__ == "__main__":
    main()