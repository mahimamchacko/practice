# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = set(ransomNote)
        for let in letters:
            if ransomNote.count(let) > magazine.count(let):
                return False
        return True