# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ind = 0
        t_ind = 0

        while s_ind < len(s) and t_ind < len(t):
            if t[t_ind] == s[s_ind]:
                s_ind += 1
            t_ind += 1
        
        return s_ind >= len(s)