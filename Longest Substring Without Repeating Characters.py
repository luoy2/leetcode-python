# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Subscribe to see which companies asked this question
import itertools


class Solution(object):
    def lengthOfLongestSubstring3(self, s):
        my_dict = {}
        start = 0
        longest = 0
        for i,v in enumerate(s):
            if v not in my_dict.values():
                my_dict[i] = v
            else:
                for k, v_1 in my_dict.items():
                    if v_1 == v:
                        pos = k+1
                for dict_key in range(start, pos):
                    my_dict.pop(dict_key)
                my_dict[i] = v
                start = pos
            longest = max(len(s[start:(i+1)]), longest)
        return longest

    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in range(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            print(s[i], s[start], longest, i - start + 1)
            longest = max(longest, i - start + 1)

        return longest

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return ""
        if len(s) == 1:
            return s
        my_dict = {}
        pos1 = 0
        while pos1 < (len(s)-1):
            list_temp = s[pos1]
            pos2 = pos1 + 1
            while pos2 < len(s) and s[pos2] not in list_temp:
                list_temp += s[pos2]
                pos2 += 1
            try:
                my_dict[len(list_temp)].append(list_temp)
            except KeyError:
                my_dict[len(list_temp)] = [list_temp]
            pos1 += 1
            print(my_dict)
        return (my_dict[max([i for i in my_dict.keys()])][0])

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring3('aaa'))
    print(Solution().lengthOfLongestSubstring3('pwwkewecaf'))
    print(Solution().lengthOfLongestSubstring3('pwwkewecaf'))
    print(Solution().lengthOfLongestSubstring3('bbbbb'))


