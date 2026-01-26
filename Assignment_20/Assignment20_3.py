
import threading


def Evenlist(lst):
    ans = 0
    for i in lst:
        if(i % 2 == 0):
            ans =  ans + i
    print(ans)

def OddList(lst):
    ans = 0
    for i in lst:
        if(i % 2 != 0):
            ans =  ans + i
    print(ans)


def main():
    lst = [1,2,3,4,5,6,7,8,9,10]
    t1 = threading.Thread(target=Evenlist,args=(lst,))
    t2 = threading.Thread(target=OddList,args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()