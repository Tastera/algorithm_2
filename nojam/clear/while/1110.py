import sys
a = int(sys.stdin.readline())
end = a
cnt = 0

if a < 10:
    a += 10*a
    cnt += 1
else:
    a = (a%10)*10 + (a//10 + a%10)%10
    cnt += 1

while a != end:
    if a < 10:
        a += 10*a
        cnt += 1
    else:
        a = (a%10)*10 + (a//10 + a%10)%10
        cnt += 1
    
print(cnt)