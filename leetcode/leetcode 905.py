# https://leetcode.com/problems/sort-array-by-parity/

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            odd = nums[left] % 2 == 1
            even = nums[right] % 2 == 0
            if even and odd:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
            else:
                if not(odd):
                    left += 1
                if not(even):
                    right -= 1
        
        return nums