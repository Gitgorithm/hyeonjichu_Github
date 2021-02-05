n=int(input())
stack=[]
ans=[]
count=1
result=True
for i in range(1,n+1):
    data=int(input())
    while count<=data:
        stack.append(count)
        count+=1
        ans.append('+')
    if stack[-1]==data:
        stack.pop()
        ans.append('-')
    else:
        result=False
if result:
    print('\n'.join(ans))
else:
    print('NO')
