import time



n, m = map(int,input().split())
start_time = time.time()
d = []
for i in range(n) :     # 세로
    d.append([])
    a = input().split()
    for j in range(m) :     # 가로
        d[i].append(0)
        d[i][j] = int(a[j])     #d[세로][가로]
        a.sort(reverse=True)

min = 0

for i in range(n) :
    if i == 0 :
        min = d[0][m-1]
    elif d[i][m-1] > d[i-1][m-1] :
        min = d[i][m-1]
    else :
        min = d[i-1][m-1]

print(min)
end_time = time.time()
print("시간 :", end_time - start_time)
