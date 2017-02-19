# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


# Arguments: In mathematics we have learnt that any number that is divisible by 9, the sum of the digits in the number is also divisible by 9. Also, here we know that the result of the problem is an integer lying in the range [0,9] .



# Proof
# The proof for the divisibility rule for 9 is essentially the same as the proof for the divisibility rule for 3.
# For any integer x written as an· · · a3a2 a1a0 we will prove that if 9|(a0 + a1+ a2+ a3 ... + an), then 9|x and vice versa.
#
# First, we can state that
#  x = a0 + a1×10 + a2×102 + a3×103... + an×10n
#
# Next if we let s be the sum of its digits then
#
# s = a0 + a1 + a2 + a3 + ... + an .
#
# So
# x - s = (a0 - a0) + (a1 × 10 - a1) + (a2×102 - a2) + ... + (an×10n - an)
#                                = a1(10 - 1) + a2(102 - 1) + ... + an(10n - 1).
# If we let bk = 10k - 1, then bk = 9...9 (9 occurs k times) and bk ­=9(1…1) and we can rewrite the previous equation as
# x - s = a1(b1)+ a2(b2)+ ... + an (bn)
# It follows that all numbers bk are divisible by 9, so the numbers ak×bk are also divisible by 9. Therefore, the sum of all the numbers ak×bk  (which is x-s) is also divisible by 9.
#
# Since x-s is divisible by 9, if x is divisible by 9, then so is s and vice versa.

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return (0)
        elif num % 9 == 0:
            return (9)
        else:
            return (num % 9)