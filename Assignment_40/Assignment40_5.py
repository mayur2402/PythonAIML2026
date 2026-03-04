import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    fileName = 'student_performance_ml.csv'
    df = pd.read_csv(fileName)

    X = df.drop('FinalResult',axis=1)
    Y = df['FinalResult']

    X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.1)

    model = DecisionTreeClassifier()

    model.fit(X_Train,Y_Train)

    y_Pred = model.predict(X_Test)
    print('Predicted values')
    print(y_Pred)
    print('Actual Values')
    print(Y_Test)

    correct = 0
    arr = np.array(Y_Test)

    for i in range(len(y_Pred)):
        if y_Pred[i] == arr[i]:
            correct = correct + 1
    
    print(correct)
    print('Accuracy of model is ', (correct*100)/len(y_Pred))

if __name__ == "__main__":
    main()