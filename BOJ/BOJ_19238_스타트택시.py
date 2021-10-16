from collections import deque
import copy

n, m, oil = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]
taxi = list(map(int, input().split()))
taxi[0] -= 1
taxi[1] -= 1
people = [list(map(int, input().split())) for x in range(m)]
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]  #상하좌우 반복하는 방향

#출발지(start)부터 갈 수 있는 모든 곳의 거리를 구하는 함수
def distance(start):
    a = copy.deepcopy(arr)
    a[start[0]][start[1]] = 1
    queue = deque()
    queue.append(start)
    while queue:
        s = queue.popleft()
        x = s[0]
        y = s[1]
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 0:
                    queue.append([nx, ny])
                    a[nx][ny] = a[x][y] + 1
    return a


while len(people) > 0:
    d = []  #[승객 위치x, 위치y, 거리, 인덱스] 담을 배역
    d_arr = distance(taxi)  #출발지부터 모든 거리 계산한 배열
    for i in range(len(people)):    #모든 승객의 위치를 계산
        px = people[i][0]-1
        py = people[i][1]-1
        d.append([px, py, d_arr[px][py]-1, i])
    d.sort(key= lambda x: (x[2], x[0], x[1]))   #주어진 조건에 맞춰 거리, 행, 열 순으로 정렬
    if d[0][2] == -1:    #거리가 -1이 나올 수 없음 => 막혀있는 경우
        oil = -1
        break
    idx = d[0][3]   #people의 인덱스
    oil -= d[0][2]  #거리가 필요한 연료이므로 빼줌
    if oil < 0:    #승객한테 갈 수 없음
        oil = -1
        break
    taxi = [people[idx][0] - 1, people[idx][1] - 1] #택시가 손님의 위치로 이동함
    d_arr = distance(taxi)
    dist = d_arr[people[idx][2]-1][people[idx][3]-1]-1  #목적지까지의 거리
    oil -= dist
    if oil < 0: #목적지 도착 못함
        oil = -1
        break
    oil += dist * 2
    taxi = [people[idx][2]-1, people[idx][3]-1] #택시가 손님 목적지로 이동함
    del people[idx] #도착한 손님은 배열에서 제거
print(oil)
