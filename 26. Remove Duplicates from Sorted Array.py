# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
#
# Subscribe to see which companies asked this question.

# My Approach

nums = [1,1,2]
# pos = 0
# limit = len(nums) - 1
# while pos < limit:
#     if nums[pos] == nums[pos + 1]:
#         nums[pos:] = nums[(pos + 1):]
#         limit -= 1
#         pos -= 1
#     pos += 1
# print (len(nums))

# Time Limit Exceeded

# Approach 2:
# 先检测需要替换的位置 标记为i， 然后从i开始把每一个不同的数往后填
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if len(nums) >= 2:
            while i < len(nums) - 1:
                if nums[i + 1] == nums[i]:
                    i += 1
                    j = i
                    while j < len(nums) - 1:
                        if nums[j] != nums[j + 1]:
                            nums[i] = nums[j + 1]
                            i += 1
                        j += 1
                    return (i)
                i += 1
        else:
            return (len(nums))



