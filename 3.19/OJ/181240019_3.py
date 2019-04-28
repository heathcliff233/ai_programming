def fac(x):
    sum = 0
    for i in range(1,int(x/2)+1):
        if x % i == 0 :
            sum += i
    return sum
n = 10
for i in range(2,n+1):
    if (i == fac(i)):
        print(i)
