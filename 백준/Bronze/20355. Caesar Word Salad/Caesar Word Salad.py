d = 26
data = input()
for i in range(26) :
    if data.count(chr(97+i)) > 0 :
        d -= 1
print(d if d!=0 else "impossible")