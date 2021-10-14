import itertools

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]

chicken = []
people = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i, j])
        elif arr[i][j] == 1:
            people.append([i, j])
people = people
ans = []
new_arr = list(itertools.combinations(chicken, m))
for i in range(len(new_arr)):
    answer = 0
    for j in range(len(people)):
        tmp = 9999
        for k in range(len(new_arr[i])):
            tmp = min(tmp, abs(people[j][0] - new_arr[i][k][0]) + abs(people[j][1] - new_arr[i][k][1]))
        answer += tmp
    ans.append(answer)
print(min(ans))