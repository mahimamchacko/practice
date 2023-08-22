# https://leetcode.com/problems/find-the-highest-altitude/

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        highest = 0

        for alt in gain:
            curr += alt
            highest = max(curr, highest)
        
        return highest