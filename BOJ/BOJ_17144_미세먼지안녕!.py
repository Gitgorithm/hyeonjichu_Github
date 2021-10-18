import copy

r, c, l = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(r)]

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]  #상하좌우 검사
air = []

for x in range(l):  #l번 반복(l초 후)
    dust = [[0] * c for x in range(r)]
    for i in range(r):
        for j in range(c):
            cnt = 0 #상,하,좌,우 몇 개로 확산됐는지 표시
            if arr[i][j] == -1:
                air.append(i)
                continue
            elif arr[i][j] >= 5:    #5보다 작은 경우는 5로 나눈 몫이 0이므로 할 필요 없다.
                for k in range(4):
                    nx = i + direction[k][0]
                    ny = j + direction[k][1]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:   #공기 청정기의 위치는 빼야한다.
                        dust[nx][ny] += arr[i][j]//5
                        cnt += 1
            dust[i][j] += arr[i][j] - (arr[i][j]//5)*cnt

    #회전 반시계
    dust[0].append(0)
    l = dust[0][0]
    del dust[0][0]

    dust[air[0]].insert(0,0)
    rr = dust[air[0]][-1]
    del dust[air[0]][-1]

    lx = air[0]
    rx = 0
    for i in range(air[0]):
        if i == air[0] - 1:
            dust[lx][0] = l
            dust[rx][c-1] = rr
            dust[air[0]][0] = -1    #공기 청정기 위치는 -1로 지정
        else:
            dust[lx][0] = dust[lx-1][0]
            dust[rx][c-1] = dust[rx+1][c-1]
            lx -= 1
            rx += 1

    #회전 시계
    dust[air[1]].insert(0, 0)
    rr = dust[air[1]][-1]
    del dust[air[1]][-1]

    dust[-1].append(0)
    l = dust[-1][0]
    del dust[-1][0]

    lx = air[1]
    rx = r-1
    for i in range(r-air[1]-1):
        if i == r-air[1]-2:
            dust[lx][0] = l
            dust[rx][c-1] = rr
            dust[air[1]][0] = -1    #공기 청정기 위치는 -1로 지정
        else:
            dust[lx][0] = dust[lx+1][0]
            dust[rx][c-1] = dust[rx-1][c-1]
            lx += 1
            rx -= 1
    arr = copy.deepcopy(dust)

print(sum(sum(dust, []))+2)

