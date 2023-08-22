# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        length = min(len(word1), len(word2))
        
        for i in range(length):
            word += (word1[i] + word2[i])
        
        if len(word1) > len(word2):
            word += word1[length:]
        elif len(word2) > len(word1):
            word += word2[length:]
        
        return word