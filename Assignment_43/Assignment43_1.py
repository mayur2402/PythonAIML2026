import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

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

def LabelEncodeing(data):
    Whetherle = LabelEncoder()
    data['Whether'] = Whetherle.fit_transform(data['Whether'])

    Temperaturele = LabelEncoder()
    data['Temperature'] = Temperaturele.fit_transform(data['Temperature'])

    Playle = LabelEncoder()
    data['Play'] = Playle.fit_transform(data['Play'])

    return (data,Playle)

def SplitData(Data):
    X = Data[['Whether','Temperature']]
    Y = Data['Play']

    return(X,Y)

def TrainData(X,Y):
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)
    return model
    
def TestModel(model,X_test):
    y_pred = model.predict(X_test)
    return y_pred

def main():
    fileName = 'PlayPredictor.csv'
    data = ReadFile(fileName)
    print(data)

    cleandata = CleanData(data)

    print(cleandata)

    labeleddata,Playle = LabelEncodeing(cleandata)

    X,Y = SplitData(labeleddata)

    print(X)
    print(Y)

    model = TrainData(X,Y)

    testDf = pd.DataFrame({
        'Whether' : [1,2,0],
        'Temperature' : [0,1,2]
    })

    y_Pred = TestModel(model,testDf)

    print(y_Pred)

    actual_values = Playle.inverse_transform(y_Pred)

    print(actual_values)

if __name__ == "__main__":
    main()