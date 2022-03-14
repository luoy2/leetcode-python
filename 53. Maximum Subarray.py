# 53. Maximum Subarray Add to List
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            print(i, nums[i], dp[i])
        return dp[-1]


self = Solution()
self.maxSubArray(nums)


class Solution:
    def maxSubArray(self, nums) -> int:
        pre = nums[0]
        max_ = pre
        for i in range(1, len(nums)):
            print(i, pre, max_)
            pre = max(nums[i], pre + nums[i])
            max_ = max(max_, pre)
            print(pre, max_)
        return max_


self = Solution()
self.maxSubArray([5, 4, -1, 7, 8])


# 贪心

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        res = -1e5
        for i in nums:
            sum_ += i
            res = max(res, sum_)
            if sum_ < 0:
                sum_ = 0
        return res