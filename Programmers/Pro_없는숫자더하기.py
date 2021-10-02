import collections

def solution(numbers):
    answer = 0
    num = list(range(0,10))
    answer = collections.Counter(num)-collections.Counter(numbers)
    return sum(answer)