# https://leetcode.com/problems/maximum-subarray/submissions/

# Solution 1 -  Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            max_num = max(max_num, nums[i])
        return max_num
