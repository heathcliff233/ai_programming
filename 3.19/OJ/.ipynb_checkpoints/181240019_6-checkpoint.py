x = int(input())
while(x != 1):
    if (x % 2 == 1):
        print('{0}*3+1={1}'.format(x,3*x+1))
        x = 3*x + 1
    else:
        print('{0}/2={1}'.format(x,x//2))
        x = x // 2
