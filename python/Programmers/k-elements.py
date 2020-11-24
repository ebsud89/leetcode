def solution(array, commands):
    answer = []

    for cmd in commands:
        sliced = array[cmd[0]-1: cmd[1]]
        k = cmd[2]
        sort = sorted(sliced)
        answer += [sort[k-1]]
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, command))