class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price
            else:
                profit = price - min_price  # Calculate profit
                max_profit = max(max_profit, profit)  # Update max_profit if needed
                
        return max_profit
