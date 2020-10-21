from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        idx = 0
        up = True
        down = False
        if (len(A)<3):
            return False
        if (A[0] > A[1]):
            return False

        for key in A[1:]:
            if up:
                if A[idx] > key:
                    up = False
                    down = True
            else:
                if A[idx] <= key:
                    down = False
            idx += 1

        if not up and down:
            return True
        else:
            return False


s = Solution()
arr = [0, 3, 2, 1]
print(s.validMountainArray(arr))
arr = [2,1]
print(s.validMountainArray(arr))
arr = [9,8,7,6,5,4,3,2,1,0]
print(s.validMountainArray(arr))
arr = [3,5,5]
print(s.validMountainArray(arr))
