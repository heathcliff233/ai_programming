n = int(input())
arr = []
for i in range(n):
    a = list(input().split())
    arr.append(a)
sum = 0
for i in range(n):
    sum += int(arr[i][i])
    sum += int(arr[i][n-1-i])
if (n%2==1):
    p = int((n-1)/2)
    sum -= int(arr[p][p])
print(sum)
