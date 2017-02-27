# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Subscribe to see which companies asked this question.

# First Approach: time exceeds limit
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return (1)
        else:
            return (self.climbStairs(n-1) + self.climbStairs(n-2))

# Memoization


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.solver(n, {})

    def solver(self, n, dict):
        if n in dict:
            return (dict[n])
        elif n <= 1:
            dict[n] = 1
            return (dict[n])
        else:
            dict[n] = (self.solver(n - 1, dict) + self.solver(n - 2, dict))
            return dict[n]

# Other's iterative:
class Solution:
    """
    :type n: int
    :rtype: int
    """
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current