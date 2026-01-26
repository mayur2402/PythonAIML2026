#Write a program which display first 10 even numbers on screen.
#Output:
#2 4 6 8 10 12 14 16 18 20




def main():
    i = 0
    j = 2
    while(i != 10):
        print(j, end="\t")
        j = j+2
        i = i+1
    
if __name__ == "__main__":
    main()