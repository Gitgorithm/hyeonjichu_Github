n = int(input())
li = [list(map(int,input().split())) for i in range(n)]
dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    if i + li[i][0] > n:   #주어진 기간 내에 끝내지 못하는 경우
        dp[i] = dp[i+1]
    else:
        dp[i] = max(li[i][1] + dp[i+li[i][0]], dp[i+1])
print(dp[0])