from itertools import *
ran, size = map(int, input().split())
li = list(range(1,ran+1))
#li = list(map(int,input().split()))
for i in sorted(product(li, repeat = size)) :
  print(" ".join(list(map(str,i))))