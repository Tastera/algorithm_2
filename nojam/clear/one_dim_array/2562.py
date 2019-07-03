import sys
max_num = 0
max_idx = 0
for i in range(9):
    a = int(sys.stdin.readline())
    if max_num < a:
        max_num = a
        max_idx = i+1
print(max_num)
print(max_idx)