# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maximum = 0
        left, right = 0, 0
        n = len(s)
        while right < k:
            if s[right] in vowels:
                maximum += 1
            right += 1
        
        curr = maximum
        while right < n:
            if s[left] in vowels:
                curr -= 1
            if s[right] in vowels:
                curr += 1
            maximum = max(maximum, curr)
            
            left += 1
            right += 1
        
        return maximum
