# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

# Solution 1 - SLOW

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diffList = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        maxProfit = 0 if not len(diffList) else diffList[0]
        for i in range(1, len(diffList)):
            diffList[i] = max(diffList[i] + diffList[i-1], diffList[i])
            maxProfit = max(diffList[i], maxProfit)
        return 0 if maxProfit < 0 else maxProfit


# Solution 2

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]
        for i in prices:
            lowest = min(lowest, i)
            profit = i - lowest
            maxProfit = max(profit, maxProfit)
        return maxProfit
