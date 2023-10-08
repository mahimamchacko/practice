# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        length = len(nums) 

        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                nums[left] = nums[right]
                right -= 1
                length -= 1
        
        return length