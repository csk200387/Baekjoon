while 1 :
    a, b, c = sorted(map(int, input().split()))
    if [a, b, c] == [0, 0, 0] :
        break
    else :
        if a**2 + b**2 == c**2 :
            print("right")
        else :
            print("wrong")