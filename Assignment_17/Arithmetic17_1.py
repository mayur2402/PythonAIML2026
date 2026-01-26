
def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def multi(no1,no2):
    return no1*no2

def div(no1,no2):
    try:
        return no1/no2
    except:
        print("Exception")
        return "Invalid input"