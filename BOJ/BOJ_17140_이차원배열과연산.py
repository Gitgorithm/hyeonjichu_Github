from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(3)]

r -= 1
c -= 1
time = 0


def sort1():
    s = 0
    for i in range(len(arr)):
        key = list(Counter(arr[i]).keys())
        value = list(Counter(arr[i]).values())
        tmp = []
        for j in range(len(key)):
            if key[j] != 0:
                tmp.append([key[j], value[j]])
        tmp.sort(key=lambda x: (x[1], x[0]))
        arr[i] = sum(tmp, [])
        s = max(len(arr[i]), s)
    for i in range(len(arr)):
        if len(arr[i]) != s:
            n = s - len(arr[i])
            arr[i] += [0] * n


while 1:
    if len(arr) > r and len(arr[0]) > c:
        if arr[r][c] == k:
            break
    time += 1
    if time > 100:
        time = -1
        break
    if len(arr) >= len(arr[0]):
        sort1()
    else:
        arr = list(map(list, zip(*arr)))
        sort1()
        arr = list(map(list, zip(*arr)))

print(time)
