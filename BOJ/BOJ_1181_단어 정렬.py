num = int(input())
data = []
max_num = 0     #data list의 가장 긴 단어의 길이

for i in range(num):
    x=input()
    data.append(x)
    if max_num < len(x):    #가장 긴 단어의 길이 저장
        max_num = len(x)

cnt=[[] for i in range(max_num+1)]      #단어의 길이로 나눌 빈 리스트 생성
print(cnt)
for i in data:  #단어 길이가 같은 것끼리 분류
    if i not in cnt[len(i)]:    #중복 제거
        cnt[len(i)].append(i)

print(cnt)
for i in range(1, max_num+1):
    cnt[i].sort()   #정렬 시킨 후, 출력
    for j in range(len(cnt[i])):
        print(cnt[i][j])
print(cnt)

