poem_EN1 = input()
poem_EN = poem_EN1.lower()
poem_list = poem_EN.split()
p_dict = {}
for item in poem_list:
    if item[-1] in ',.\'"!':
        item = item[:-1]
    p_dict[item] = p_dict.get(item, 0) + 1
lst1 = list(p_dict)
lst2 = [p_dict[i] for i in lst1]
all = list(zip(lst1 , lst2))
all1 = sorted(all,key = lambda x : (x[1],x[0]),reverse = False)
for j in range(len(all1)):
    print(all1[j][0],all1[j][1])
