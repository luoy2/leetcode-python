# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
#
# Subscribe to see which companies asked this question.


# My approach: recursion
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return (0)
        elif len(nums) == 1:
            return nums[0]
        else:
            return (self.solver(0, nums, {}))

    def solver(self, n, nums, my_dict):
        if n in my_dict:
            pass
        elif n == len(nums) - 1:
            my_dict[n] = (nums[n])
        elif n == len(nums) - 2:
            my_dict[n] = max(nums[n], nums[n+1])
        else:
            my_dict[n] = max(self.solver(n+1, nums, my_dict), nums[n] + self.solver(n+2, nums, my_dict))
        return (my_dict[n])

test1 = Solution()
print(test1.rob([1,2,3,2,1]))



# Other Approach:
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0

        if len(num) == 1:
            return num[0]

        num_i, num_i_1 = max(num[1], num[0]), num[0]
        for i in range(2, len(num)):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(num[i] + num_i_2, num_i_1);

        return num_i

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
