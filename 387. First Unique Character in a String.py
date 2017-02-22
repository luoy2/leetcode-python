# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

# First Approach:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for element in s:
            try:
                count[element] += 1
            except:
                count[element] = 1
        temp_lst = [i for i in s if count[i] == 1]
        if temp_lst:
            return (list(s).index(str(temp_lst[0])))
        else:
            return (-1)
# Run Time Exceeds

# Second Approach:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for element in s:
            try:
                count[element] += 1
            except:
                count[element] = 1
        ans = -1
        for i, element in enumerate(s):
            if count[element]==1:
                return (i)
        return (-1)

# Other's one line version:
class Solution(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])
