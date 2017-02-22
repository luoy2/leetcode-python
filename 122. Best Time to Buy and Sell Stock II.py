# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).




# My Approach: find the consecutive sublist in the list and get the sum
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        day = 0
        while day < len(prices)-1:
            if prices[day+1] <= prices[day]:
                day+=1
            else:
                day2 = day + 1
                while day2 < len(prices) - 1:
                    if prices[day2 + 1] < prices[day2]:
                        break
                    day2 += 1
                ans += prices[day2] - prices[day]
                day = day2
        return (ans)

# Since you can hold only one transaction at 1 time:
class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

    