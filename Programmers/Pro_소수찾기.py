import itertools, math


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    num = []
    for i in range(1, len(numbers) + 1):
        num += list(itertools.permutations(numbers, i))
    for i in range(len(num)):
        num[i] = int(''.join(list(num[i])))
    num = list(set(num))
    for i in num:
        if i >= 2:
            chk = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    chk = False
                    break
            if chk:
                answer += 1

    return answer