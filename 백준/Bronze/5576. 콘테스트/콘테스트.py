W = [int(input()) for i in range(10)]
K = [int(input()) for i in range(10)]
W.sort()
K.sort()
print(sum(W[7:]),sum(K[7:]))