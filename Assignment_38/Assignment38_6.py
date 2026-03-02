import pandas as pd
import matplotlib.pyplot as plt

def main():
    fileName = 'student_performance_ml.csv'

    df = pd.read_csv(fileName)

    plt.figure()
    plt.hist(df['StudyHours'])
    plt.xlabel('Study Hours')
    plt.ylabel('No of student')
    plt.show()

if __name__ == "__main__":
    main()