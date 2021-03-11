import sys
from itertools import combinations
 
l, c = map(int, sys.stdin.readline().split())
data = sorted(list(sys.stdin.readline().split()))
VOWELS = set('aeiou') # 모음
 
cm = list(combinations(data, l))    #가능한 조합을 리스트로 만들기
cm.sort()   #순서대로 정렬
for c in cm:
    diff = set(c).difference(VOWELS)    #차집합 => 자음만 남음
    if 1 < len(diff) < l:
        print(''.join(c))
        continue

