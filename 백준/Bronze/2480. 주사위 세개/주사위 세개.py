d1, d2, d3 = map(int, input().split())

if d1 == d2 == d3 :
    print(10000 + d1 * 1000)
elif d1 == d2 or d1 == d3 :
    print(1000 + d1 * 100)
elif d2 == d3 :
    print(1000 + d2 * 100)
else :
    if d1 > d2 and d1 > d3 :
        print(d1*100)
    elif d2 > d1 and d2 > d3 :
        print(d2*100)
    else :
        print(d3*100)