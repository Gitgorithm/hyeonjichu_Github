import sys
from itertools import combinations

input=sys.stdin.readline

def solve(case):
    if sum(case)==100:  #합이 100인 경우 
        case=list(case)
        case.sort()
        for i in case:
            print(int(i))
        return True
    return False
        

if __name__ == "__main__":
    data=set()  #집합 자료형
    for i in range(9):
        height=int(input().strip())     #양쪽 공백 모두 삭
        data.add(height)
        
    for case in combinations(data,7):   #입력된 data중에서 중복없이 7개 선택
        if solve(case):
            break
