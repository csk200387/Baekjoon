def eratosthenes(a, b):
    arr = [True for _ in range(b+1)]
    arr[0] = arr[1] = False
    for i in range(2, b+1) :
        if arr[i] :
            for j in range(i*i, b+1, i) :
                arr[j] = False

    for i in range(a, b+1) :
        if arr[i] :
            if str(i) == str(i)[::-1] :
                print(i)

a, b = map(int,input().split())
if b > 10_000_000 :
    b = 10_000_000
if a > 10_000_000 :
    a = 10_000_000
    if b > 10_000_000 :
        b = 10_000_000
eratosthenes(a,b)
print(-1)