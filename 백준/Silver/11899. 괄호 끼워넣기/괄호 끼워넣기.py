d=input()
s=[d[0]]
for i in range(1, len(d)):
 s.append(d[i])
 if len(s)>=2 and s[-1]==")" and s[-2]=="(":
  s.pop()
  s.pop()
print(len(s))