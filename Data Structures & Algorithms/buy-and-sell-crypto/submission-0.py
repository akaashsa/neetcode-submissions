class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = prices[-1]
        profit = 0
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            else:
                profit = max(profit, max_price - prices[i])
        return profit