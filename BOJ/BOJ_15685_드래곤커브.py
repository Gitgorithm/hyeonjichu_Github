n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]

direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]  #0, 1, 2, 3 각 시작 방향


def find(i, j, x, y):   #90도 회전했을 때 위치
    nx = -(j - y) + x
    ny = i - x + y
    return nx, ny


def move(arr):  #마지막 점 기준으로 모두 회전시키기
    tmp = []
    for i in range(len(arr)-1):
        nx, ny = find(arr[i][0], arr[i][1], arr[-1][0], arr[-1][1])
        tmp.append([nx, ny])
    tmp.reverse()
    return arr + tmp


q = []
for i in range(len(arr)):
    x = arr[i][0] + direction[arr[i][2]][0]
    y = arr[i][1] + direction[arr[i][2]][1]
    tmp = [[arr[i][0], arr[i][1]], [x, y]]
    #세대만큼 반복하기
    for j in range(arr[i][3]):
        tmp = move(tmp)
    #중복 제거하기 위함
    for k in tmp:
        if [k[0], k[1]] not in q:
            q.append(k)
ans = 0
d = [[-1, 0], [-1, 1], [0, 1]]
#꼭지점 모두 있는 사각형 찾기
for i in range(len(q)):
    x = q[i][0]
    y = q[i][1]
    chk = True
    for k in range(3):
        if [x+d[k][0], y+d[k][1]] not in q:
            chk = False
            break
    if chk:
        ans += 1
print(ans)