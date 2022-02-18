# https://leetcode.com/problems/remove-element/submissions/

# Solution 1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        i = 0
        while i < len(nums) and i <= last:
            if nums[i] == val:
                tmp = nums[i]
                nums[i] = nums[last]
                nums[last] = tmp
                last -= 1
                i -= 1
            i += 1
        return last + 1
