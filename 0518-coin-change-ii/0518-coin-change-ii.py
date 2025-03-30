class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] += dp[current_amount - coin]
        
        return dp[amount]

        