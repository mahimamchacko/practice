# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1

        for letter in t:
            letters[letter] -= 1
        
        for letter in letters.keys():
            if letters[letter] != 0:
                return False
        return True