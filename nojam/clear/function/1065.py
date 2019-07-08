import sys

def f(n):
    global res
    if int(str(n)[2]) - int(str(n)[1]) == int(str(n)[1]) - int(str(n)[0]):
        res[n] = 1

n = int(sys.stdin.readline())
if n < 100:
    print(n)
else:
    res = [0] + [1]*99 + [0]*900
    for i in range(100, n+1):
        f(i)
    print(res.count(1))