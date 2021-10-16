n, m = map(int, input().split())
robot = list(map(int, input().split()))
arr = [list(map(int, input().split())) for x in range(n)]
visited = [[False]*m for x in range(n)]
direction = {0:[0, -1], 3:[1, 0], 2:[0, 1], 1:[-1, 0]}    #북, 서, 남, 동

c = 0   #회전 몇 번 했는지
visited[robot[0]][robot[1]] = True
ans = 1
while True:
    #왼쪽 검사
    lx = robot[0] + direction[robot[2]][0]
    ly = robot[1] + direction[robot[2]][1]
    if visited[lx][ly] == False and arr[lx][ly] == 0:   #왼쪽을 청소할 수 있는 경우
        c = 0   #청소를 하면 회전한 값을 초기화 해야 함
        robot[2] = (robot[2] - 1) % 4
        robot[0] = lx
        robot[1] = ly
        visited[lx][ly] = True
        ans += 1
    else:   #왼쪽 청소할 수 없으면 회전하기
        c += 1
        robot[2] = (robot[2] - 1) % 4
        if c == 4:  #4번을 회전하면 모든 방향을 모두 검사한 것이므로 후진할 수 있는지 검사
            c = 0
            chk = (robot[2] - 1) % 4
            cx = robot[0] + direction[chk][0]
            cy = robot[1] + direction[chk][1]
            if arr[cx][cy] == 1:    #뒤가 벽이면 후진할 수 없고 청소 끝
                print(ans)
                break
            else:   #벽이 아니면 후진하고 다시 왼쪽부터 검사
                robot[0] = cx
                robot[1] = cy
