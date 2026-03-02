
import pandas as pd

def main():
    fileName = 'student_performance_ml.csv'

    df = pd.read_csv(fileName)

    print('Total No of students are :')
    print(df.shape[0])

    print('Total No of students passed are :')
    print((df[df['FinalResult'] == 1]).shape[0])

    print('Total No of students failed are :')
    print((df[df['FinalResult'] == 0]).shape[0])

if __name__ == "__main__":
    main()