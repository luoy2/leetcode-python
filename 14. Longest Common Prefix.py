# Write a function to find the longest common prefix string amongst an array of strings.


# My approach:
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return("")
        elif len(strs) == 1:
            return(strs[0])
        else:
            i = 0
            limit = min([len(x) for x in strs])
            if not limit:
                return ("")
            else:
                while i < limit:
                    temp_str = [str[i] for str in strs]
                    if temp_str.count(temp_str[0]) != len(temp_str):
                        return(strs[0][:i])
                    i += 1
                return(strs[0][:i])

strs= ['a', 'b']
Solution().longestCommonPrefix(strs)