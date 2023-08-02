def maxProfit(prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                prof = prices[i] - prices[i-1]
                max_profit += prof
        return max_profit