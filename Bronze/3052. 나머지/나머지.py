dic = {}
for i in range(0,10):
    num = int(input("")) % 42
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
print(len(dic.keys()))