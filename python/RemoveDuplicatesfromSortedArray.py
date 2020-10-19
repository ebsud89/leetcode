class Solution:
    def removeDuplicates(self, nums) -> int:
#         idx = 0
#         cnt = 0
#         for key in nums:
#             if(key != nums[idx]):
#                 idx += 1
#                 if (idx > len(nums)):
#                     break
#             else:
#                 nums[idx] = key
#                 cnt += 1
#         print(nums)
#         return cnt

        idx = 1
        for i in range(0, len(nums)):
            if i != 0 and nums[i - 1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        print(idx)
        return idx

s = Solution()
s.removeDuplicates([1, 1, 2])
s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

a = set([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(a)
print(list(a))