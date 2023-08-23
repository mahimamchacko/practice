# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occs = defaultdict(int)
        for val in arr:
            occs[val] += 1
        return len(set(occs.values())) == len(occs.values())