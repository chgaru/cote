n = int(input())
a = 0

for i in range(n+1) :
    if i == 3 or i == 13 or i == 23 :
        a += 3600   # 60 * 60
    else :
        a += 1575   # (15*60 * 2) - (15*15)
print(a)