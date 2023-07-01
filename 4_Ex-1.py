n = int(input())
move = list(input().split())

x = 1; y = 1

for i in move :
    if i == "r" :
        y += 1
    elif i == "l" :
        y -= 1
    elif i == "u" :
        if x == 1 :
            continue
        else :
            x -= 1
    elif i == "d" :
        if x == n :
            continue
        else :
            x += 1
print(x,y)
