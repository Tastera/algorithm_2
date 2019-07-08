def d(n):
    if n < 10:
        return 2*n
    else:
        for i in str(n):
            n += int(i)
        return n

res = [0]*10001
for i in range(1, 10001):
    if d(i) <= 10000:
        res[d(i)] = 1
        
for i in range(1, len(res)):
    if res[i] == 0:
        print(i)