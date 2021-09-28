def solution(clothes):
    answer = 1
    list1, list2 = map(list, zip(*clothes))
    body = list(set(list2))
    for i in range(len(body)):
        answer = answer*(list2.count(body[i])+1)
    return answer-1