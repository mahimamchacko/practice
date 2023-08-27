# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []
        
        for char in s:
            if char in opening:
                stack.append(char)
            elif len(stack) == 0 or char != opening[stack.pop()]:
                return False
        
        return len(stack) == 0