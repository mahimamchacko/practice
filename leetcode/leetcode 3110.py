class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        
        vals = {}
        vals[s[0]] = ord(s[0])
        for i in range(len(s) - 1):
            left = s[i]
            right = s[i + 1]
            if right not in vals:
                vals[right] = ord(right)
            score += abs(vals[left] - vals[right])
        
        return score