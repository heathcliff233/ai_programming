n = 10
strr = ''
for i in range(1,n+1):
    strr += str(i)
for j in range(0,10):
    print('%d '%strr.count(str(j)),end='')
 
