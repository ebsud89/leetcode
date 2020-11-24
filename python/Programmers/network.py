def solution(n, computers):
    def dfs(i, j):
        if i < 0 or i >= n or \
                j < 0 or j >= n or \
                computers[i][j] != 1:
            return

        computers[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                dfs(i, j)
                count += 1
    return count





test1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # 2
test2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] # 1

print(solution(3, test1))
print(solution(3, test2))