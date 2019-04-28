import sys
s= 0
for x in sys.argv[1:]:
    s+=eval(x)
print(s)
