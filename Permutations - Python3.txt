Permutations - Leetcode 

Recursive Solution Python3

import sys

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        permutations = []
        for i in nums:
            list_diff = list(set(nums) - set([i]))
            rest_permutations = self.permute(list_diff)
            for perm in rest_permutations:
                permutations.append([i] + perm)
        return permutations