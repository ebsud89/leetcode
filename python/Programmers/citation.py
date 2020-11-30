import collections


def solution(citations):
    pcnt = len(citations)
    mid = pcnt // 2
    sorted_list = sorted(citations)

    while True:
        if sorted_list[mid] <= len(sorted_list[mid:]):
            mid += 1
        elif sorted_list[mid] > len(sorted_list[:mid]):
            mid -= 1
            break
        else:
            break

    print(sorted_list)
    print(mid)
    return sorted_list[mid]


citation1 = [3, 0, 6, 1, 5]	# 3
#print(solution(citation1))
citation2 = [0, 1, 1]	# 1

#print(solution(citation2))

c1 = 'a'
c2 = 'b'
print(c1 > c2)
c3 = "asdfbkldasdgrasdfcf"
counter = collections.Counter(c3)
print(counter['a'])