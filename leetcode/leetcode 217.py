# https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for num in nums:
            if hashmap[num] > 0:
                return True
            hashmap[num] += 1
        return False