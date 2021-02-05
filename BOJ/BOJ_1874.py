num=int(input())
stack=[]
for i in range(num):
    stack.append(int(input()))
n=0
chk=True
ans=[]
for i in range(0, int(stack[0])):
    ans.append('+') #처음 수 까지 순서대로 push
    n+=1
ans.append('-') #push하고 마지막 값은 stack[0]과 같으므로 pop

for i in range(1, num):
    if int(stack[i-1])-1==stack[i]:  #하나 작으면 오름차순 이므로 pop
        ans.append('-')
    elif int(stack[i-1])<stack[i]:   #큰 수면 그 수만큼 push하고 하나 pop
        for j in range(n, int(stack[i])):
            ans.append('+')
            n+=1
        ans.append('-')
    elif int(stack[i-1])>stack[i]:   #2이상 작을경우
        for j in range(int(stack[i-1])-1,int(stack[i]), -1):
            for k in range(0, i-1):
                if j == int(stack[k]):
                    chk=True
                    break
                else:
                    chk=False
        if chk==False:
            ans.append('NO')
        ans.append('-')
    else:
        ans.append('NO')
#답 출력
if 'NO' in ans:
    print('NO')
else:
    for i in range(len(ans)):
        print(ans[i])
