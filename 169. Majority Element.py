# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.



# My approach:
# O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        pos = 0
        ans = nums[0]
        print(nums[pos], count, ans)
        while pos < len(nums) - 1:
            pos += 1
            if nums[pos] != ans:
                if count == 0:
                    ans = nums[pos]
                    count += 1
                else:
                    count -= 1
                    if not count:
                        ans = None
            else:
                count += 1

        return (ans)


# O(nlog(n))
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) / 2]