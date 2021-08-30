def solution(scores):
    new_list = list(map(list, zip(*scores)))
    for i in range(len(scores)):
        if new_list[i].count(new_list[i][i]) == 1 and (new_list[i][i] == max(new_list[i]) or new_list[i][i] == min(new_list[i])):
            del new_list[i][i]
        mean = sum(new_list[i])/len(new_list[i])
        if mean >= 90:
            new_list[i] = 'A'
        elif 80 <= mean < 90:
            new_list[i] = 'B'
        elif 70 <= mean < 80:
            new_list[i] = 'C'
        elif 50 <= mean < 70:
            new_list[i] = 'D'
        elif mean < 50:
            new_list[i] = 'F'

    return ''.join(new_list)