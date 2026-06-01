class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left, right = 0, 1 
        # max_profit = 0
        # while(right < len(prices)):
        #     if(prices[left] < prices[right]):
        #         curr_profit = prices[right] - prices[left]
        #         max_profit = max(curr_profit, max_profit)
        #     else:
        #         left = right 
        #     right += 1
        # return max_profit   

        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            curr_profit = prices[r] - prices[l]
            while(curr_profit < 0 and l < r):
                l += 1
            max_profit = max(curr_profit, max_profit)
        return max_profit