# https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        num = 0
        for hour in hours:
            if hour >= target:
                num += 1
        return num