import sys
a = sys.stdin.readline()
b = list(map(int, sys.stdin.readline().split()))
b.sort()
print(b[0], b[-1])