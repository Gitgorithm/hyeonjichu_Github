def solution(priorities, location):
    num = [x for x in range(len(priorities))]
    new_list = list(map(list, zip(priorities, num)))
    order = [[-1,-1]]
    while order[-1][1] != location:
        for i in range(len(priorities)):
            if new_list[0][0] != max(priorities):
                tmp = new_list[0]
                new_list.remove(new_list[0])
                new_list.append(tmp)
            else:
                tmp = new_list[0]
                priorities.remove(new_list[0][0])
                new_list.remove(new_list[0])
                order.append(tmp)
                break
    return len(order)-1