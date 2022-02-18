# https://leetcode.com/problems/search-insert-position/submissions/

# Solution 1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return mid if nums[mid] > target else mid + 1
