class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_buy = (0, float('inf'))
        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price-min_buy)
        return max_profit