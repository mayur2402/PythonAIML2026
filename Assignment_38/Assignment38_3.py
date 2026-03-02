import pandas as pd

def main():
    fileName  = 'student_performance_ml.csv'
    df = pd.read_csv(fileName)

    avg = df['StudyHours'].mean()
    print('Average of study hours are :',avg)

    avg = df['Attendance'].mean()
    print('Average of Attendance is :', avg)

    max = df['PreviousScore'].max()
    print('Maximum of previous score is :', max)

    min = df['PreviousScore'].min()
    print('Minimun of previous score is :', min)

if __name__ == "__main__":
    main()