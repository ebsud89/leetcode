from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_arr, odd_arr = [], []

        for key in A:
            if key%2 == 0:
                even_arr.append(key)
            else:
                odd_arr.append(key)

        print(even_arr)
        print(odd_arr)

        return even_arr + odd_arr

s = Solution()
arr = [3,1,2,4]
print(s.sortArrayByParity(arr))