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

    con = confusion_matrix(Y_Test,y_Pred)

    print(con)

    y_train_pred = model.predict(X_Train)

    accuracy = accuracy_score(Y_Train,y_train_pred)

    print('Training accuracy is : ', accuracy*100)

    model = DecisionTreeClassifier(max_depth=1)

    model.fit(X_Train,Y_Train)

    y_Pred = model.predict(X_Test)

    accuracy = accuracy_score(Y_Test,y_Pred)

    print('Accuracy with max_depth = 1 is : ', accuracy*100)

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(X_Train,Y_Train)

    y_Pred = model.predict(X_Test)

    accuracy = accuracy_score(Y_Test,y_Pred)

    print('Accuracy with max_depth = 3 is : ', accuracy*100)

    print(X_Train)
    
    new_data = pd.DataFrame([{
    'StudyHours': 6,
    'Attendance': 85,
    'PreviousScore': 66,
    'AssignmentsCompleted': 7,
    'SleepHours': 7
    }])
    
    y_pred = model.predict(new_data)
    if y_pred:
        print('User will passed')
    else:
        print('User will failed')

if __name__ == "__main__":
    main()