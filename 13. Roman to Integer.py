# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {"I":1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i, elem in enumerate(s):
            if i > 0 and my_dict[elem] > my_dict[s[i-1]]:
                ans += my_dict[elem] - 2*my_dict[s[i-1]]
            else:
                ans += my_dict[elem]
        return(ans)
