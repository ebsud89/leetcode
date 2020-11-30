import collections

class Solution:
    def hammingWeight(self, n: int) -> int:
        string = str(bin(n))

        counter = collections.Counter(string)
        print(counter)

        return counter['1']





s = Solution()

str1 = 0o00000000000000000000000000001011 # 3
print(s.hammingWeight(str1))

str2 = 0o11111111111111111111111111111101 # 31
print(s.hammingWeight(str2))