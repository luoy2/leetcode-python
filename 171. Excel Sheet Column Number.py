# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

#  My approach:
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dict = {}
        count = 1
        ans = 0
        for element in letter:
            dict[element] = count
            count += 1

        letter_num = len(s) - 1
        for target_s in s:
            ans += dict[target_s] * (26 ** letter_num)
            letter_num -= 1
        return (ans)


# One line python
class Solution:
# @param s, a string
# @return an integer
def titleToNumber(self, s):
    l = list(s)
    l.insert(0,0)
    return reduce(lambda x,y: 26*x+ord(y)-64, l)

l = list('AAC')
list(filter(lambda x: x != 'A', l))