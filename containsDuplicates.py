# https://leetcode.com/problems/contains-duplicate/submissions/

# Solution 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for j, i in enumerate(nums):
            if i in seen:
                return True
            seen[i] = j
        return False

# Solution 2 - kinda cheating


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
