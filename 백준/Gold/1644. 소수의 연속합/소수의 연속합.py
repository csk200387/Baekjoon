def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]


n = int(input())
arr = prime_numbers(n)
cnt = 0
start, end = 0, 0
s = 0

while True:
    try:
        if s >= n:
            s -= arr[start]
            start += 1
        elif s < n:
            s += arr[end]
            end += 1
        if s == n:
            cnt += 1

    except IndexError:
        break

print(cnt)