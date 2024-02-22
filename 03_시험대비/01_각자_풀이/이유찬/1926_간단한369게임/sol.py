n = int(input())

for i in range(1, n+1):
    s = str(i)
    count = 0
    for j in s:
        if (j == '3') or (j == '6') or (j == '9'):
            count += 1
    if count == 0:
        print(i, end=" ")
    else:
        print(count * '-', end=" ")