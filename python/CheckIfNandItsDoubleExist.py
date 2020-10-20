
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        res = False
        for key in arr:
            cnt = arr.count((key*2))
            if cnt != 0:
                if key == 0:
                    if cnt == 2:
                        res = True
                    else:
                        res = False
                else:
                    res = True
                    break
        return res


s = Solution()
arr = [0,0]
print(s.checkIfExist(arr))
arr = [-20,8,-6,-14,0,-19,14,4]
print(s.checkIfExist(arr))
arr = [-2,0,10,-19,4,6,-8]
print(s.checkIfExist(arr))