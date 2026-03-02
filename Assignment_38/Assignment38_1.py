import pandas as pd

def main():
    fileName = 'student_performance_ml.csv'

    data = pd.read_csv(fileName)

    border = '-'*50
    print(border)
    print(data)
    print(border)
    
    print('First five records are :')
    print(border)
    print(data.head())
    print(border)

    print('Last five records are :')
    print(border)
    print(data.tail())
    print(border)

    print("Total Rows and Columns:")
    print(data.shape)
    print(border)

    print("List of column name")
    print(data.columns.tolist())
    print(border)

    print("Data type ")
    print(data.dtypes)
    print(border)

if __name__ == '__main__':
    main()