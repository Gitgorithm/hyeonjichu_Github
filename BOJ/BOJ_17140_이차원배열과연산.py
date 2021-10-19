from collections import Counter

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(3)]

#인덱스 하나씩 줄이기
r -= 1
c -= 1
time = 0

#조건에 맞게 정렬 시키는 함수
def sort():
    s = 0
    for i in range(len(arr)):
        key = list(Counter(arr[i]).keys())
        value = list(Counter(arr[i]).values())
        tmp = []
        for j in range(len(key)):
            if key[j] != 0: #0인 경우는 정렬하지 않음
                tmp.append([key[j], value[j]])
        tmp.sort(key=lambda x: (x[1], x[0]))
        arr[i] = sum(tmp, [])
        s = max(len(arr[i]), s)

    #가장 긴 길이에 맞춰서 0 채우기
    for i in range(len(arr)):
        if len(arr[i]) != s:
            n = s - len(arr[i])
            arr[i] += [0] * n
            arr[i] = arr[i][:100]


while 1:
    #조건 맞으면 중단, 범위 맞지 않을 수 있음 indexError 조심하기
    if len(arr) > r and len(arr[0]) > c:
        if arr[r][c] == k:
            break
    time += 1
    if time > 100:  #100초가 지나면 안됨
        time = -1
        break
    #행 정렬
    if len(arr) >= len(arr[0]):
        sort()
    #열 정렬
    else:
        arr = list(map(list, zip(*arr)))
        sort()
        arr = list(map(list, zip(*arr)))

print(time)
