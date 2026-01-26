
def ChkPrime(no):
    isprime = True
    if no == 2:
        return True
    for i in range(2,int(no/2)+1):
        if(no%i == 0):
            isprime = False
            break
    return isprime