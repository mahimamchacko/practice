# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one = set(nums1)
        two = set(nums2)
        
        res1 = []
        res2 = []

        for val in one:
            if val not in two:
                res1.append(val)
        
        for val in two:
            if val not in one:
                res2.append(val)

        return [res1, res2]