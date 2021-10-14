from collections import deque

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for x in range(k)]#사과 위치
l = int(input())
order = deque([list(input().split()) for x in range(l)])#회전 명령

direction = [[0,1], [1, 0], [0,-1],[-1,0]]
time = 0
s = deque([[0, 0]])
t, d = order.popleft()  #시간, 회전 방향
idx = 0 #방향(direction)은 오른쪽 부터 시작이므로 0번부터 시작, 오른쪽 회전은 +1, 왼쪽 회전은 -1
while 0 <= s[-1][0]+direction[idx][0] < n and 0 <= s[-1][1]+direction[idx][1] < n:
    x = s[-1][0]+direction[idx][0]
    y = s[-1][1]+direction[idx][1]
    if [x, y] not in s:
        s.append([x, y])
        time += 1
        if [x+1, y+1] in apple:
            apple.remove([x+1,y+1])
        else:
            s.popleft()
        if time == int(t):
            if d == 'L':
                idx = (idx - 1) % 4
            elif d == 'D':
                idx = (idx + 1) % 4
            if len(order) > 0:
                t, d = order.popleft()
    else:
        break
print(time+1)