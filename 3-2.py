n, m, k = map(int,input().split())  # 배열크기, 더해지는 횟수, 중복 제한
l = list(map(int,input().split()))
l.sort(reverse = True)

a = 0
total = 0
count = 0
while count != m :
    for i in range(k) :
        a += l[0]
        count += 1
        print("l[0]을 더했습니다.")
        if count == m :
            break
    a += l[1]
    count += 1
    print("l[1]을 더했습니다.")


print(a)
print(count)
