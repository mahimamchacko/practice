# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp = x
        y = 0
        while temp > 0:
            y *= 10
            y += temp % 10
            temp = temp // 10
        
        return y == x