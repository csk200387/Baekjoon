t = int(input())
s = 0
for _ in range(int(input())) :
  a, b = map(int, input().split())
  s += a*b
print("Yes" if s == t else "No")