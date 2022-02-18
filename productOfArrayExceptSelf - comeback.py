# https://leetcode.com/problems/product-of-array-except-self/submissions/

# Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        productArray = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            if zeroCount > 1:
                break
        if zeroCount > 1:
            for i in range(len(nums)):
                productArray.append(0)
            return productArray

        product_zero = 1
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                product_zero = 0
            else:
                product *= nums[i]
                product_zero *= nums[i]

        for i in range(len(nums)):
            if nums[i] == 0:
                productArray.append(product)
            else:
                productArray.append(floor(product_zero * (nums[i] ** -1)))
        return productArray


# Solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
