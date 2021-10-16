from collections import deque

n, k = map(int, input().split())
queue = deque(list(map(int, input().split())))
robot = deque([0] * n * 2) #로봇이 존재하면 1, 없으면 0
ans = 0

while True:
    ans += 1
    tmp = queue.pop()
    queue.appendleft(tmp)
    tmp2 = robot.pop()
    robot.appendleft(tmp2)
    if any(robot):  #로봇이 있으면 이동하기
        if robot[n-1] == 1: #내리는 위치에 있으면 바로 내린다.
            robot[n-1] = 0
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and queue[i+1] >= 1:
                if i+1 != n-1:
                    robot[i + 1] = 1
                robot[i] = 0
                queue[i+1] -= 1
    if queue[0] != 0:
        robot[0] = 1
        queue[0] -= 1
    if queue.count(0) >= k:
        print(ans)
        break