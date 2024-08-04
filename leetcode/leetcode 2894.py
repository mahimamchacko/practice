# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum = 0

        for i in range(n + 1):
            if i % m == 0:
                sum -= i
            else:
                sum += i
        
        return sum