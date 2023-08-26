# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            other_i = hashmap.get(target - val)
            if other_i is None:
                hashmap[val] = i
            else:
                return [other_i, i]
        