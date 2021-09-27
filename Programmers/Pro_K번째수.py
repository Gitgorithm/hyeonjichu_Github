def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new_list = array[commands[i][0]-1:commands[i][1]]
        new_list.sort()
        answer.append(new_list[commands[i][2]-1])
    return answer