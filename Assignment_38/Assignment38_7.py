import pandas as pd
import matplotlib.pyplot as plt

def main():
    fileName = 'student_performance_ml.csv'

    df = pd.read_csv(fileName)

    passed = df[df['FinalResult'] == 1]
    failed = df[df['FinalResult'] == 0]

    plt.figure()
    plt.scatter(passed['StudyHours'],passed['PreviousScore'],label = 'pass')
    plt.scatter(failed['StudyHours'],failed['PreviousScore'],label = 'fail')
    plt.xlabel('Study Hours')
    plt.ylabel('Previous Score')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()