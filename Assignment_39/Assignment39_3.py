import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    fileName = 'student_performance_ml.csv'
    df = pd.read_csv(fileName)

    X = df.drop('FinalResult',axis=1)
    Y = df['FinalResult']

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2)

    model = DecisionTreeClassifier()

    model.fit(X_Train,Y_Train)

    y_Pred = model.predict(X_Test)
    print('Predicted values')
    print(y_Pred)
    print('Actual Values')
    print(Y_Test)

    accuracy = accuracy_score(Y_Test,y_Pred)

    print('Accuracy of model is ', accuracy * 100)
if __name__ == "__main__":
    main()