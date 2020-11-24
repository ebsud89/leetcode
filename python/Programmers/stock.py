def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for key, price in enumerate(prices[1:]):
        stack.append(price)
        print("key : ", key, "stack : ", stack)
        for ret in stack:
            print(ret)
            if prices[key] < ret:
                answer[key] += 1

    return answer


test = [1, 2, 3, 2, 3] # [4, 3, 1, 1, 0]
print(solution(test))