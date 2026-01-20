#Write a program which accepts marks and displays grade.
#Condition Example:
#≥ 75 → Distinction
#≥ 60 → First Class
#≥ 50 → Second Class
#< 50 → Fail

def DisplayGrade(marks):
    if(marks>=75 and marks <=100):
        print("Distinction")
    elif(marks>=60 and marks <75):
        print("First Class")
    elif(marks>=50 and marks <60):
        print("Second Class")
    elif(marks>=1 and marks <50):
        print("Fail")
    else:
        print("Enter valid marks")

def main():
    print("Enter marks to displays grade")
    marks = int(input())
    DisplayGrade(marks)


if __name__ == "__main__":
    main()