# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Subscribe to see which companies asked this question.

# My approach: 简单粗暴
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = 0
        if digits:
            for i, elem in enumerate(digits):
                ans += elem*10**(len(digits) - i - 1)
        ans += 1
        return ([int(i) for i in str(ans)])

