sentence = 'This is a sentence a.'
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
all1 = sorted(all,key = lambda x : (x[1],x[0]),reverse = False)
for j in range(len(all1)):
    print(all1[j][0],all1[j][1])
