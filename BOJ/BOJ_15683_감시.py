import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]
d = [[-1, 0], [0, -1], [1, 0], [0, 1]]  #상, 좌, 하, 우
directions = [[],
              [[0], [1], [2], [3]],
              [[0, 2], [1, 3]],
              [[0, 1], [1, 2], [2, 3], [3, 0]],
              [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
              [[0, 1, 2, 3]]
              ]


def find(x, y, direction, arrc):
    for k in direction:
        nx = x
        ny = y
        while 0 <= nx+d[k][0] < n and 0 <= ny+d[k][1] < m:
            nx += d[k][0]
            ny += d[k][1]
            if arrc[nx][ny] != 6:
                if arrc[nx][ny] == 0:
                    arrc[nx][ny] = '#'
            else:
                break


def dfs(a, cnt):
    global ans
    tmp = copy.deepcopy(a)
    if cnt == len(cctv):
        c = 0
        for i in range(len(tmp)):
            c += tmp[i].count(0)
        ans = min(ans, c)
        return
    cc, x, y = cctv[cnt]
    for i in range(len(directions[cc])):
        find(x, y, directions[cc][i], tmp)
        dfs(tmp, cnt+1)
        tmp = copy.deepcopy(a)


ans = 9999
cctv = []
for i in range(n):
    for j in range(m):
        if arr[i][j] in range(1, 6):
            cctv.append([arr[i][j], i, j])
dfs(arr, 0)
print(ans)