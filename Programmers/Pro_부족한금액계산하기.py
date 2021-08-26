def solution(price, money, count):
    answer = -1
    sum_list = [(price * (x + 1)) for x in range(count)]
    if sum(sum_list) - money > 0:
        answer = sum(sum_list) - money
    else:
        answer = 0

    return answer
