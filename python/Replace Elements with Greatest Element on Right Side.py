from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        idx = 1
        while idx < len(arr):
            arr2 = arr[idx:]
            maxi = max(arr2)
            arr[idx-1] = maxi
            idx += 1
        arr[idx-1] = -1

        return arr

s = Solution()

arr = [17,18,5,4,6,1]
print(arr)
print(s.replaceElements(arr))
