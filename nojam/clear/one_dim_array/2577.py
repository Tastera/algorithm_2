import sys
res = [0]*10
a = 1
for i in range(3):
    a *= int(sys.stdin.readline())
for i in str(a):
    res[int(i)] += 1 
for i in res:
    print(i)