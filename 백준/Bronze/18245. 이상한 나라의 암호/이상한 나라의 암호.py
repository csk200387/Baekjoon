i = 2
while 1:
    s = input()
    if s == "Was it a cat I saw?":
        break
    print(s[::i])
    i += 1