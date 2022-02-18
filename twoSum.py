# https://leetcode.com/problems/two-sum/submissions/


# Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = [[i, nums[i]] for i in range(len(nums))]
        numList.sort(key=lambda num: num[1])
        i = 0
        j = len(numList) - 1
        while numList[i][1] + numList[j][1] != target:
            if numList[i][1] + numList[j][1] > target:
                j -= 1
            elif numList[i][1] + numList[j][1] < target:
                i += 1
            else:
                break
        return [numList[i][0], numList[j][0]]

# Solution 2


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            j = target-nums[i]
            if(j in hashmap):
                return [hashmap[j], i]
            hashmap[nums[i]] = i
