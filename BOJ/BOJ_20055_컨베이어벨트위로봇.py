from collections import deque

n, k = map(int, input().split())
queue = deque(list(map(int, input().split())))
robot = deque([0] * n * 2) #로봇이 존재하면 1, 없으면 0
ans = 0

while True:
    ans += 1
    #컨베이어 벨트를 회전시킨다.
    queue.appendleft(queue.pop())
    robot.appendleft(robot.pop())
    if any(robot):  #로봇이 있으면 이동하기
        if robot[n-1] == 1: #내리는 위치에 있으면 바로 내린다.
            robot[n-1] = 0
        for i in range(n-2, -1, -1):    #하나씩 검사해서 이동 가능하면 이동시킨다.
            if robot[i] == 1 and robot[i+1] == 0 and queue[i+1] >= 1:
                if i+1 != n-1:  #이동한 위치가 내리는 위치이면 바로 내린다.
                    robot[i + 1] = 1
                robot[i] = 0
                queue[i+1] -= 1
    if queue[0] != 0:   #맨 앞에 로봇을 올리수 있으면 올린다.
        robot[0] = 1
        queue[0] -= 1
    if queue.count(0) >= k: #내구도가 0인 것이 k개 이상이면 중단한다.
        print(ans)
        break