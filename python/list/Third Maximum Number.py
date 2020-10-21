from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 2:
            cnt = 3
            while len(nums) > 1 and cnt > 1:
                maxi = max(nums)
                nums.remove(maxi)
                cnt -= 1
            third = max(nums)
        else:
            third = max(nums)

        return third

s = Solution()
arr = [3, 2, 1] # 1
print(s.thirdMax(arr))
arr = [1, 2] # 2
print(s.thirdMax(arr))
arr = [2, 2, 3, 1] # 1
print(s.thirdMax(arr))