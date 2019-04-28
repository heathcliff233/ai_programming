Code = input()
Set1=set('12345')
Set2=set('6789')
Set2.add('10')
SingersPicked = set('479122622169745579554')
Line1 = []
Line2 = []
Line3 = []

for number in SingersPicked:
    Line1.append(number)
print(sorted(Line1))
Set3 = Set1 & SingersPicked
for number in Set3:
    Line2.append(number)
print(sorted(Line2))
Set4 = Set2.difference(SingersPicked)
for number in Set4:
    Line3.append(number)
print(sorted(Line3))


if Code in SingersPicked:
     print('Y')
else:
     print('N')
