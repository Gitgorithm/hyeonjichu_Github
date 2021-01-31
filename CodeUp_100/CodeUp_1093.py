students=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num=int(input())
data=[int(x) for x in input().split()]
for i in data:
    students[i-1]=int(students[i-1])+1
for i in range(23):
    print(students[i], end=' ')
