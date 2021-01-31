num=int(input())
students=list(map(int, input().split()))
for i in range(num,0,-1):
    print(students[i-1], end=' ')
