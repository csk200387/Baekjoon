al = list("abcdefghijklmnopqrstuvwxyz")
b = [-1]*26
a = input()
for i in range(len(a)-1,-1,-1) :
    b[al.index(a[i])] = a.index(a[i])
for i in b :
    print(i)