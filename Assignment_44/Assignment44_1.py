import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def ReadFile(fileName):
    try:
        fileName = pd.read_csv(fileName)
        return fileName
    except Exception as ex:
        print(ex)

def CleanData(Data):

    if 'Unnamed: 0' in Data.columns:
        try:
            Data.drop(columns = ['Unnamed: 0'], inplace=True)
        except Exception as ex:
            print(ex)

    return Data

def SplitData(Data):
    X = Data[['TV','radio','newspaper']]
    Y = Data['sales']

    return(X,Y)

def TrainData(X,Y):
    model = LinearRegression()
    model.fit(X,Y)
    return model
    
def TestModel(model,X_test):
    y_pred = model.predict(X_test)
    return y_pred

def SplitDatafortrainingtesting(X,Y):
    X_Train,X_Test,Y_Train,Y_test = train_test_split(X,Y)

    return (X_Train,X_Test,Y_Train,Y_test)

def main():
    fileName = 'Advertising.csv'
    data = ReadFile(fileName)
    print(data)

    cleandata = CleanData(data)

    print(cleandata)

    X,Y = SplitData(cleandata)

    print(X)
    print(Y)

    X_Train,X_Test,Y_Train,Y_test = SplitDatafortrainingtesting(X,Y)

    model = TrainData(X_Train,Y_Train)

    y_Pred = TestModel(model,X_Test)

    print(y_Pred)


if __name__ == "__main__":
    main()