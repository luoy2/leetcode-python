# 原题
# 实现字符串子串匹配函数strStr()。如果字符串A是字符串B的子串，则返回A在B中
# 首次出现的地址，否则返回-1。
# 注意点：
# 空字符串是所有字符串的子串，返回0
# 例子：
# 输入: haystack = "abc", needle = "bc" 输出: 1
# 输入: haystack = "abc", needle = "gd" 输出: -1

# My approach:
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length = len(needle)
        if not haystack and not needle:
            return (0)
        elif not haystack:
            return (-1)
        elif not needle:
            return (0)
        else:
            pos = 0
            while pos <= len(haystack) - needle_length:
                if haystack[pos:(pos+needle_length)] == needle:
                    return(pos)
                pos += 1
            return (-1)

