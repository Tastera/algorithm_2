import sys
# 재귀
n = int(sys.stdin.readline())

star = [["*"]*n for i in range(n)]

for i in range(1, n, 3):
    for j in range(1, n, 3):
        star[i][j] = ' '

for i in range(n//3, (n//3)*2):
    for j in range(n//3, (n//3)*2):
        star[i][j] = ' '

for i in star:
    print(''.join(i))