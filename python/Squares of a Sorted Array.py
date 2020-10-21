from typing import List

class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)

s = Solution()
arr = [-4,-1,0,3,10] # [0,1,9,16,100]

arr = [-7,-3,2,3,11] # [4,9,9,49,121]