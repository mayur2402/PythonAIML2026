import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    fileName = 'student_performance_ml.csv'
    df = pd.read_csv(fileName)

    SleepHours = df['SleepHours']
    FinalResult = df['FinalResult']

    plt.figure(figsize=(6,4))
    plt.scatter(SleepHours,FinalResult)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()