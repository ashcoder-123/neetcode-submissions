class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - minprice
            if profit > maxprofit:
                maxprofit = profit
            if prices[i] < minprice:
                minprice = prices[i]
        return maxprofit
        