def solution(operations):
    answer = []
    num = []
    for i in range(len(operations)):
        o, n = operations[i].split(' ')
        if o == "I":
            num.append(int(n))
        elif o == "D":
            if n == "1" and len(num) >= 1:
                num.remove(max(num))
            elif n == "-1" and len(num) >= 1:
                num.remove(min(num))
    if len(num)>=2:
        answer.append(max(num))
        answer.append(min(num))
    else:
        answer = [0,0]
    return answer