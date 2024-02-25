n = int(input())
arr = sorted(map(int, input().split()))

start, end = 0, n-1
mn = abs(arr[start] + arr[end])
result = (arr[start], arr[end])
while start < end:
    s = arr[start] + arr[end]
    if abs(s) < mn:
        mn = abs(s)
        result = (arr[start], arr[end])
        if mn == 0:break

    if s < 0:
        start += 1
    else:
        end -= 1
print(*result)