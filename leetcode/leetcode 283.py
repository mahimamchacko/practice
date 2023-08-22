# https://leetcode.com/problems/move-zeroes/description/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            elif len(zeros) > 0:
                nums[zeros.pop(0)] = nums[i]
                nums[i] = 0
                zeros.append(i)