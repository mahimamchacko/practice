# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                days[stackIndex] = i - stackIndex
            
            stack.append([temp, i])
        
        return days