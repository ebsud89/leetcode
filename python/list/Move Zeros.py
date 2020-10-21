from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rp, wp = 0, 0

        if len(nums) < 2:
            return

        while (rp < len(nums)):
            if (nums[rp] != 0):
                nums[wp] = nums[rp]
                if rp != wp:
                    nums[rp] = 0
                wp += 1
            rp += 1

s = Solution()
nums = [0,1,0,3,12]
s.moveZeroes(nums)
print(nums)
nums = [1]
s.moveZeroes(nums)
print(nums)
nums = [1,0]
s.moveZeroes(nums)
print(nums)