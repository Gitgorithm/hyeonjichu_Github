# import sys
# input = lambda: sys.stdin.readline()
#
# def findNum(num, k):
#     cnt = 0
#     if k == 2:
#         cnt += num+1
#     elif k == 3:
#         cnt += ((num+1)*(num+2))/2
#     else:
#         for j in range(0,num+1):
#             cnt += ((j+1)*(j+2))/2
#         k -= 1
#         if k != 3:
#             cnt += findNum(num, k)
#     return cnt
#
# n, k = map(int, input().split())
# cnt = 0
# if k == 1:
#     cnt = 1
# else:
#     cnt = findNum(n, k)
# print(int(cnt))


import sys
input = lambda: sys.stdin.readline()

n, k = map(int, input().split())
data=[1]
data += [0]*n

for i in range(1,k+1):
    for j in range(1, n+1):
        data[j]=(data[j]+data[j-1])%1000000000
print(data[n])