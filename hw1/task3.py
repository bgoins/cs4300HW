import math

def ifstruc(x):
    if (x > 0):
        return "Positive"
    elif (x < 0):
        return "Negative"
    else:
        return "Zero"

def primefunc():
    primecount = 0
    primelist = []
    primeiterator = 0

    while(primecount < 10):
        if(isprime(primeiterator)==True):
            primelist.append(primeiterator)
            primecount += 1
        primeiterator += 1

    return primelist

def isprime(y):
    if y <= 1:
        return False
    for i in range(2, int(math.sqrt(y)) + 1):
        if y % i == 0:
            return False
    return True

def whilestruc():
    sumcount = 0
    sumtotal = 0

    while(sumcount <= 100):
        sumtotal += sumcount
        sumcount += 1

    return sumtotal
