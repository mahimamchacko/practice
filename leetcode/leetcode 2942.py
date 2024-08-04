# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indexes = []
        for index, word in enumerate(words):
            if x in word:
                indexes.append(index)
        return indexes