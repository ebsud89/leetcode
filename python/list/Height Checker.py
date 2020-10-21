from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt, idx = 0, 0
        sorted_height = sorted(heights)

        while (idx < len(heights)):
            if (heights[idx] != sorted_height[idx]):
                cnt += 1
            idx += 1

        return cnt

s = Solution()
arr = [1,1,4,2,1,3] # 3
print(s.heightChecker(arr))
arr = [5,1,2,3,4] # 5
print(s.heightChecker(arr))
arr = [1,2,3,4,5] # 0
print(s.heightChecker(arr))