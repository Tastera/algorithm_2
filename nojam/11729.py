import sys
n = int(sys.stdin.readline())

def hanoi(n):
    global res
    if n == 1:
        res.append([1, 3])
    
    elif n == 2:
        return [(1, 2), (1, 3), (2, 3)]

res = []