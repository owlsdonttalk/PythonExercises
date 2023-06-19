# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for idx, i in enumerate(nums):
            if target - i in res:
                return [res[target - i], idx]
            res[i] = idx


s = Solution()
res = s.twoSum([2, 7, 11, 15], 9)
print(res)
