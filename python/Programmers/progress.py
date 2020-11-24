import math

def solution(progresses, speeds):
    length = len(progresses)
    answer = []
    times = [0] * length

    for index in range(length):
        times[index] = math.ceil((100 - progresses[index]) // speeds[index])

    print("times : " ,times)
    idx, cnt = 0, 1
    while times:
        cur = times.pop(0)
        for v in times:
            if cur < v:
                break
            cnt += 1
        for _ in range(cnt-1):

            times.pop(0)

        print(times, cnt, "idx : ", idx)
        answer.append(cnt)
        cnt = 1
        idx += 1

    return answer



progresses1 = [93, 30, 55]
speeds1= [1, 30, 5] # [2, 1]
print(solution(progresses1, speeds1))

progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = 	[1, 1, 1, 1, 1, 1] # [1,3,2]
print(solution(progresses2, speeds2))