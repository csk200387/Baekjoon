a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
bm = max(abs(e-a), abs(f-b))
dm = abs(e-c)+abs(f-d)
print('bessie'if bm < dm else 'tie' if bm==dm else 'daisy')