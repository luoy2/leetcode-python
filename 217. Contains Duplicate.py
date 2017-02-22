# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.



# My approach:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = False
        dict = {}
        if nums:
            for elem in nums:
                try:
                    dict[elem] += 1
                    return (True)
                except:
                    dict[elem] = 1
        return (ans)

    # 1 Line python:
    def containsDuplicate2(self, nums):
        return (len(nums) != len(set(nums)))