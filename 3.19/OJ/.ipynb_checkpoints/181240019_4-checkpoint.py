strr = int(input())
def letter_frequency(s):
   s = s.lower()                      #全部转小写
   l = []
   for i in [chr(x) for x in range(97,123)]:
      l.append(s.count(i))            #统计个数
   return l
print(letter_frequency(strr))
