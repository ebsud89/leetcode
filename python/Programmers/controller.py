def solution(jobs):
    answer = 0

    job_cnt = len(jobs)

    sorted_jobs = sorted(jobs, key = lambda x : x[1])

    print(sorted_jobs)

    return answer


job_list = [[0, 3], [1, 9], [2, 6]] # 9
#print(solution(job_list))

str1 = "abc zfef afcb"
str2 = "abd hcve 123"
lists = [str1, str2]
print(lists)

def func(x):
    return x.split()[1], x.split()[0]
print(func(str1))
lists.sort(key = lambda x : (x.split()[1], x.split()[0]))
print(lists)

a = 10
a -= 5 > 0
print(int(True))

str3 = "vjdifi"
for i, v in enumerate(str3, 10):
    print(i, v)