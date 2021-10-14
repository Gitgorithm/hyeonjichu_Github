import itertools
from collections import deque

n = int(input())
queue = deque(map(int, input().split()))   #숫자
queue_copy = queue.copy()
arr = list(map(int, input().split()))   #기호의 각 개수

# +:0, -:1, *:2, /:3
a_list = []
for i in range(len(arr)):
    for j in range(arr[i]):
        a_list.append(i)

chk = list(set(itertools.permutations(a_list, n-1)))
answer = []

for i in range(len(chk)):
    num = queue.popleft()
    for j in range(len(chk[i])):
        if chk[i][j] == 0:  #+
            num = num + queue.popleft()
        elif chk[i][j] == 1:    #-
            num = num - queue.popleft()
        elif chk[i][j] == 2:    #*
            num = num * queue.popleft()
        elif chk[i][j] == 3:    #/
            if num < 0 :
                num = -(-num//queue.popleft())
            else:
                num = num // queue.popleft()
    answer.append(num)
    queue = queue_copy.copy()
print(max(answer), min(answer))
