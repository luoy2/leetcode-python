# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Suppose sum equals to sum of all nums, then after m times of m we get:
        # sum + m*(n-1) = x*n
        # where x is the final number we achieved. However, it would alwasy be the min Num plus m
        # x = min(nums) + m
        # Thus we can get sum + m*(n-1) = (min(nums) + m) * n, and solve for m
        return (sum(nums) - len(nums)*min(nums))