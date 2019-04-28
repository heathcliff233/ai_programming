import sys
count = 0
for x in sys.stdin:
    print(x)
    count+=1
    if count>=5:
        break
