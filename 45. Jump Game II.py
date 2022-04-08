'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
通过次数279,349提交次数633,721

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


nums = [2,3,0,1,4]
nums = [2,4,2,1,1,1]

class Solution:
    def jump(self, nums):
        if len(nums) <= 2:
            return 1
        costs = [0] * len(nums)
        idx = len(nums) - 2
        for n in reversed(nums[:-1]):
            if n == 0:
                costs[idx] = 1e5
            else:
                costs[idx] = 1 + min(costs[idx+1:idx+1+n])
            print(idx, n, costs[idx])
            idx -= 1
        return costs[0]

