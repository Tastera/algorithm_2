import sys
for tc in range(int(sys.stdin.readline())):
    score = list(map(int, sys.stdin.readline().split()))
    sum_num = 0
    for i in range(1, score[0]+1):
        sum_num += score[i]
    avg = sum_num/score[0]
    chk = 0
    for i in range(1, score[0]+1):
        if avg < score[i]:
           chk += 1

    print("%0.3f" % round((chk/score[0])*100, 3) + "%")