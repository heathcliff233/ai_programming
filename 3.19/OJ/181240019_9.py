def moni(x):
    y = 2**x -1
    return y
def sig(x):
    flag = True
    for i in range (2,int(x**0.5)+1):
        if x%i == 0:
            flag = False
            break
    return flag
n = 2
count = 0
k = 1
while(count != n):
    k += 1
    y = moni(k)
    if (sig(y)) :
        print('{0} {1}'.format(k,y))
        count += 1
