def fac(x):
    sum = 0
    for i in range(1,int(x/2)+1):
        if x % i == 0 :
            sum += i
    return sum
n = 10000
for j in range(1,n+1):
    if (fac(j) > j):
        if (j == fac(fac(j))):
            print("{0}-{1}".format(j,fac(j)))
