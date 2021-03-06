# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

# First Approach: Exceeds Time Limits
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        pos = 0
        while pos < len(prices) -1 :
            profit = max(prices[(pos+1):]) - prices[pos]
            if profit > ans:
                ans = profit
            pos += 1
        return (ans)

# Second Approcah: 
prices = [5,3,7,1,4,2]
def maxProfit(prices):
    max_profit, min_price = 0, float("inf")
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

maxProfit(prices)