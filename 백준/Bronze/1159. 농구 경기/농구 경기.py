import sys
input = sys.stdin.readline

d={}
for i in range(int(input())):
    t = input()[0]
    if t not in d:
        d[t] = 1
    else:
        d[t] += 1

r=sorted(dict(filter(lambda x:x[1]>4, d.items())).keys())
if r:print(*r,sep="")
else:print("PREDAJA")