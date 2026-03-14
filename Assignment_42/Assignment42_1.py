

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

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

if __name__ == "__main__":
    main()