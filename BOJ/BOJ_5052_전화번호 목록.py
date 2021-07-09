import copy
import sys
input = lambda : sys.stdin.readline()

num = int(input())

for _ in range(num):
    phone = int(input())
    data = []
    for _ in range(phone):
        data.append(list(input().strip('\n')))
    data.sort(key= lambda x:(len(x)))
    for i in range(phone-1):
        data2 = copy.deepcopy(data)
        if len(data2[i]) < 10:
            for j in range(i+1, phone):
                data2[j] = data2[j][0:len(data2[i])]
        data2 = list(set(map(tuple,data2)))
        if len(data2) != phone:
            print('NO')
        else:
            print('YES')

