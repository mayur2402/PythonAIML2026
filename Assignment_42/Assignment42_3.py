import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

def main():
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    X_Sum = 0
    Y_Sum = 0

    for value in X:
        X_Sum = X_Sum + value

    for value in Y:
        Y_Sum = Y_Sum + value

    n = len(X)

    X_Mean = X_Sum/n
    Y_Mean = Y_Sum/n

    print(X_Mean)
    print(Y_Mean)

    # y = mx + c 
    # m = (sum(x-x_bar) * (Y-Y_bar)) / (sum(x - x_bar) ** 2)  

    numerator = 0.0
    denominator = 0.0

    for i in range(n):
        numerator = numerator + ((X[i] - X_Mean) * (Y[i] - Y_Mean))
        denominator = denominator + ((X[i] - X_Mean) ** 2)

    print(numerator)
    print(denominator)

    m = numerator / denominator

    print(m)

    c = Y_Mean - (m*X_Mean)

    print(c)


    print("Enter X value ")
    x = float(input())

    print('predicted y is ', m*x + c)

    x = np.linspace(1,6,n)
    y = m*x + c

    plt.plot(x,y,label = 'regration line')
    plt.scatter(X,Y,label = 'Scatter plot')
    plt.xlabel('X : Indepedant varaible')
    plt.ylabel('Y : Depedant varaible')
    plt.show()

    New_y = []

    for value in X:
        new_y = m*value + c
        New_y.append(new_y)

    print(New_y)

    meansquared = mean_squared_error(Y,New_y)

    print(meansquared)

    rsquare = r2_score(Y,New_y)

    print(rsquare)

if __name__ == "__main__":
    main()