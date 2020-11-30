import heapq


def solution1(scoville, K):
    answer = 0
    heap = []

    for num in scoville:
        heapq.heappush(heap, num)

    while len(heap) > 1:
        answer += 1
        food1 = heapq.heappop(heap)
        food2 = heapq.heappop(heap)
        new = food1 + food2 * 2
        if K < new:
            break
        heapq.heappush(heap, new)

    return answer


def solution2(scoville, K):
    answer = 1

    sorted_lsit = sorted(scoville)

    for idx, v in enumerate(sorted_lsit):
        if idx > len(sorted_lsit):
            break

        answer += 1
        if K > sorted_lsit[idx] + sorted_lsit[idx+1]*2:
            break


    return  answer

list = [1, 2, 3, 9, 10, 12]
K = 7 # 2

print(solution1(list, K))