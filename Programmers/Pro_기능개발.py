import math
def solution(progresses, speeds):
    answer = []
    date = []
    for i in range(len(progresses)):
        date.append(math.ceil((100-progresses[i])/speeds[i]))
    tmp=[]
    for i in range(1, len(date)):
        tmp.append(date[i-1])
        if i != len(date)-1 and tmp[0] < date[i]:
            answer.append(len(tmp))
            tmp = []
        if i == len(date)-1:
            if tmp[0] < date[i]:
                answer.append(len(tmp))
                answer.append(1)
            else:
                tmp.append(date[i])
                answer.append(len(tmp))

    return answer