def time_difference():
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    h = h2 - h1
    m = m2 - m1
    s = s2 - s1
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1
    print(f"{h} {m} {s}")
for i in range(3) :
    time_difference()