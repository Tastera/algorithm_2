import sys
n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
score.sort()
res = 0
for i in range(n):
    score[i] = (score[i]/score[-1])*100
    res += score[i]
print(res/n)