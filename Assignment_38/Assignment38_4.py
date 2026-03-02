import pandas as pd

def main():
    fileName = 'student_performance_ml.csv'

    df = pd.read_csv(fileName)

    fResult = df['FinalResult'].value_counts()
    print('Distribution of final result is :')
    print(fResult)

    print('Percentage calculationn is ')
    per = df['FinalResult'].value_counts(normalize=True) * 100
    print(per)

if __name__ == "__main__":
    main()