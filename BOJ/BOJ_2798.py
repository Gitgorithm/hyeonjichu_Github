n,m=map(int, input().split())
num=list(map(int, input().split()))
ans=[]
for i in range(0,n-2):
    for j in range(1,n-1):
        if j>i:
            for k in range(2, n):
                if k>j:
                    if m>=num[i]+num[j]+num[k]:
                        ans.append(num[i]+num[j]+num[k])
print(max(ans))
