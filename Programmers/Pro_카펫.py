def solution(brown, yellow):
    answer = []
    num = brown + yellow
    for i in range(num//2, 1, -1):
        if num%i == 0 and i <= int(num/i):
            if (i-2) * (int(num/i)-2) == yellow:
                answer.append(int(num/i))
                answer.append(i)
                break
    return answer