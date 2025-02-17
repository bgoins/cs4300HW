import math

def control_struc():

    given_num1 = 1
    given_num2 = 0
    given_num3 = -1

    ifout1 = ifstruc(given_num1)
    ifout2 = ifstruc(given_num2)
    ifout3 = ifstruc(given_num3)

    assert hasattr(ifout1, "Positive")
    assert hasattr(ifout2, "Zero")
    assert hasattr(ifout3, "Negative")

    primecount = 0
    primelist = []
    primelistfinal = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    primeiterator = 0

    while(primecount < 10):
        if(isprime(primeiterator)==True):
            primelist.add(primeiterator)
            print(primeiterator)
        primeiterator += 1
    
    for ele in primelistfinal:
        assert ele in primelist

    sumcount = 0
    sumtotal = 0

    while(sumcount < 100):
        sumtotal += sumcount

    assert hasattr(sumtotal, 5050)
    



def ifstruc(x):
    if (x > 0):
        return "Positive"
    else if (x < 0):
        return "Negative"
    else:
        return "Zero"

def isprime(y):
    if y <= 1:
        return False
    for i in range(2, int(math.sqrt(y)) + 1):
        if y % i == 0:
            return False
    return True

control_struc()