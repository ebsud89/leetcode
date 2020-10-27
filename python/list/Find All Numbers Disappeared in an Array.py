from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for key in range(1, len(nums)+1):
            cnt = nums.count(key)
            if cnt == 0:
                nums.append(key)
        return nums

s = Solution()
arr = [4,3,2,7,8,2,3,1] # [5,6]
print(s.findDisappearedNumbers(arr))