from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(0, len(nums)):
            if i != 0 and nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx

s = Solution()

nums = [1,1,2]
print(s.removeDuplicates(nums))
print(nums)