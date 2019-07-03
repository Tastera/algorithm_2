import sys
for tc in range(int(sys.stdin.readline())):
    a = sys.stdin.readline()
    res = 0
    chk = 0
    for i in range(len(a)):
        if a[i] == "O":
            chk += 1
            res += chk
        else:
            chk = 0
    print(res)