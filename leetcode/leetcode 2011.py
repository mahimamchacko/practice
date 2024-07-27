# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }

        res = 0
        for op in operations:
            res += ops[op]
        return res