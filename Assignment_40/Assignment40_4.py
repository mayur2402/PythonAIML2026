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

    accuracy = accuracy_score(Y_Test,y_Pred)

    print('Accuracy of model is ', accuracy * 100)

    importance = model.feature_importances_
    features_importance = pd.DataFrame({'Features' : X.columns,'importance':importance})
    print(features_importance)

    new_data = pd.DataFrame([{
    'StudyHours': 6,
    'Attendance': 85,
    'PreviousScore': 66,
    'AssignmentsCompleted': 7,
    'SleepHours': 7
    },
    {
    'StudyHours': 2,
    'Attendance': 100,
    'PreviousScore': 80,
    'AssignmentsCompleted': 1,
    'SleepHours': 10
    },{
    'StudyHours': 8,
    'Attendance': 80,
    'PreviousScore': 90,
    'AssignmentsCompleted': 10,
    'SleepHours': 8
    },{
    'StudyHours': 5,
    'Attendance': 75,
    'PreviousScore': 76,
    'AssignmentsCompleted': 5,
    'SleepHours': 7
    },{
    'StudyHours': 10,
    'Attendance': 100,
    'PreviousScore': 0,
    'AssignmentsCompleted': 0,
    'SleepHours': 9
    }])
    
    y_Pred = model.predict(new_data)

    print(y_Pred)

if __name__ == "__main__":
    main()