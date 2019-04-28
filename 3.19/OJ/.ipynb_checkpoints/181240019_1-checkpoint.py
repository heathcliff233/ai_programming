def fac(x):
    sum = 0
    for i in range(1,int(x/2)+1):
        if x % i == 0 :
            sum += i
    return sum
n = int(input())
for j in range(1,n+1):
    if (fac(x) > x):
        if (x == fac(fac(x))):
            print("{0}-{1}".format(x,fac(x)))
