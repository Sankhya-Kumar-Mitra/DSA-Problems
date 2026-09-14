class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        currentPrice = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<currentPrice:
                currentPrice = prices[i]
            result = max(prices[i]-currentPrice,result)
        return result
            