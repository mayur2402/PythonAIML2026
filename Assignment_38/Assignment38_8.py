import pandas as pd
import matplotlib.pyplot as plt

def main():
    fileName = 'student_performance_ml.csv'

    df = pd.read_csv(fileName)

    attendance = df['Attendance'].tolist()

    plt.figure()
    plt.boxplot(x=attendance)
    plt.title('Box plot for Attendance')
    plt.ylabel('Attendance')
    plt.show()

if __name__ == "__main__":
    main()