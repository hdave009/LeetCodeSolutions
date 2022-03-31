# https://leetcode.com/problems/container-with-most-water/submissions/

# Solution 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start = 0
        end = len(height) - 1
        while start < end:
            h = min(height[start], height[end])
            w = end - start
            if w * h > maxArea:
                maxArea = w * h
            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1
                end -= 1

        return maxArea
