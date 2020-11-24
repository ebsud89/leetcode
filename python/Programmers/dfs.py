def solution(numbers, target):
    answer = 0
    length = len(numbers)
    result = []
    path = []

    def dfs(csum, index, path):
        if index == length+1:
            if csum == 0:
                result.append(1)
            return

        operation = [-1, 1]
        for op in operation:
            dfs(csum + numbers[index-1] * op, index+1, path + [numbers[index-1]*op])

    dfs(target, 1, path)

    return result.count(1)


numbers = [1, 1, 1, 1, 1]
target = 3
ret = solution(numbers, target)
print(ret)