sentence = input()
sentence1 = sentence.replace(',','')
sentence2 = sentence1.replace('.','')
sentence3 = sentence2.replace('\'','')
sentence4 = sentence3.replace('?','')
sentence5 = sentence4.replace(':','')
sentence6 = sentence5.replace('"','')
sentence7 = sentence6.replace(';','')
sentence8 = sentence7.lower()
lst = sentence8.split()
import collections
dic1 = collections.Counter(lst)
lst1 = list(dic1)
lst2 = [dic1[i] for i in lst1]
all = list(zip(lst1 , lst2))
print(all)
all1 = sorted(all,key = lambda x : x[1],reverse = False)
for j in range(len(all2)):
    print(all2[j][0],all2[j][1])