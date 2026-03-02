import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    fileName = 'student_performance_ml.csv'
    df = pd.read_csv(fileName)

    AssignmentsCompleted = df['AssignmentsCompleted']
    FinalResult = df['FinalResult']

    plt.figure(figsize=(6,4))
    plt.scatter(AssignmentsCompleted,FinalResult)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()