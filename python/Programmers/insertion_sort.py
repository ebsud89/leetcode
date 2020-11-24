import collections

def to_swap(n1: int, n2: int) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)

def insertion_sort(list) -> str:
    answer = []
    i = 1
    while i < len(list):
        j = i
        while j>0 and to_swap(list[j - 1], list[j]):
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1
        i += 1

    return str(int(''.join(map(str, list))))

list = [3, 30, 34, 5, 9]
print(insertion_sort(list))

str = "AABC"
t="AB"
need = collections.Counter(str)
missing = len(t)
for right, char in enumerate(str,1):
    print(right, " : ", char)
    missing -= need[char] > 0
    print(missing)