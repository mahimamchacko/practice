# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        num = 1
        for i in range(len(nums)):
            result[i] *= num
            num *= nums[i]
        
        num = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= num
            num *= nums[i]
        
        return result