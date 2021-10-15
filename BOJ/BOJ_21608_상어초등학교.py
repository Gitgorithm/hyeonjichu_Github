n = int(input())
s = [list(map(int, input().split())) for x in range(n*n)]   #학생과 좋아하는 학생 리스트
arr = [[0]*n for _ in range(n)] #자리 배열

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상, 하, 좌, 우
for i in range(len(s)):     #전체 학생
    tmp = arr.copy()
    ans = []    #[j, k, 좋아하는 사람, 비어있는 자리]
    for j in range(len(tmp)):   #배열
        for k in range(len(tmp[j])):
            if tmp[j][k] == 0:
                p = 0   #people
                e = 0   #empty
                for l in range(4):    #direction
                    nj = j + direction[l][0]
                    nk = k + direction[l][1]
                    if 0 <= nj < n and 0 <= nk < n:
                        if tmp[nj][nk] == 0:
                            e += 1
                        elif tmp[nj][nk] != 0 and tmp[nj][nk] in s[i][1:]:
                            p += 1
                ans.append([j, k, p, e])
    ans.sort(reverse=True, key= lambda x : (x[2], x[3], -x[0], -x[1]))
    arr[ans[0][0]][ans[0][1]] = s[i][0]

answer = {}

for i in range(n):
    for j in range(n):
        answer[arr[i][j]] = [i, j]
result = 0
for i in range(len(s)):
    ans = 0
    for j in range(1, 5):
        t = abs(answer[s[i][0]][0]-answer[s[i][j]][0]) + abs(answer[s[i][0]][1] - answer[s[i][j]][1])
        if t == 1:
            ans += 1
    if ans == 0:
        result += 0
    elif ans == 1:
        result += 1
    elif ans == 2:
        result += 10
    elif ans == 3:
        result += 100
    elif ans == 4:
        result += 1000
print(result)