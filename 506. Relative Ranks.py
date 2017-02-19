# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
#
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.



# My approach:
# Create a dictionary of each score's rank
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return ([])
        sorted_nums = sorted(nums)
        dict = {}
        rank = len(sorted_nums)
        for element in sorted_nums:
            dict[element] = str(rank)
            rank -= 1

        if len(nums) >= 1:
            dict[sorted_nums[-1]] = "Gold Medal"
        if len(nums) >= 2:
            dict[sorted_nums[-2]] = "Silver Medal"
        if len(nums) >= 3:
            dict[sorted_nums[-3]] = "Bronze Medal"

        return ([dict[i] for i in nums])


# Other's approach:
def findRelativeRanks(self, nums):
    rank = dict((n, i + 1) for i, n in enumerate(sorted(nums, reverse=True)))
    return [["Gold Medal", "Silver Medal", "Bronze Medal"][rank[x] - 1] if rank[x] <= 3 else str(rank[x]) for x in nums]