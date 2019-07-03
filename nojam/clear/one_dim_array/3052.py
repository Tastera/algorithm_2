import sys
res = []
for i in range(10):
    a = int(sys.stdin.readline()) % 42
    if a not in res:
        res.append(a)
print(len(res))