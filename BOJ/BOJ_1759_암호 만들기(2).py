from itertools import combinations
 
L, C = map(int, input().split())
data = set(input().split())
 
A = set(['a', 'e', 'i', 'o', 'u'])  #모음
 
word_list = data & A    #data와 A의 모음 리스트
 
for i in combinations(sorted(data), L):
    num = len(set(i) & word_list)   #모음 개수
    if num == 0 or L-num < 2: continue  #모음이 없거나 자음(L-num)이 2개가 아니면
    print(''.join(i))

