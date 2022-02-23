'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
'''


# simple approach:
import re
def is_alpha(c):
    return 65 <= ord(c) <= 90 or ord(c) >= 97


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        new_s = list(s)
        j = len(new_s) - 1
        for _, c in enumerate(s):
            if is_alpha(c):
                while not is_alpha(new_s[j]):
                    j -= 1
                new_s[j] = c
                j -= 1
        return ''.join(new_s)


s = 'a-bC-d'
Solution().reverseOnlyLetters("7_28]")
Solution().reverseOnlyLetters("a-bC-dEf-ghIj")


## other solution
# 双指针
'''
思路与算法

我们使用 \textit{left}left 指针从左边开始扫描字符串 ss，\textit{right}right 指针从右边开始扫描字符串 ss。如果两个指针都扫描到字母，且 \textit{left} < \textit{right}left<right，那么交换 s[\textit{left}]s[left] 和 s[\textit{right}]s[right]，然后继续进行扫描；否则表明反转过程结束，返回处理后的字符串。

代码

Python3C++JavaC#CGolangJavaScript

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        left, right = 0, len(ans) - 1
        while True:
            while left < right and not ans[left].isalpha():  # 判断左边是否扫描到字母
                left += 1
            while right > left and not ans[right].isalpha():  # 判断右边是否扫描到字母
                right -= 1
            if left >= right:
                break
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是字符串 ss 的长度。反转过程需要 O(n)O(n)，C 语言计算字符串长度需要 O(n)O(n)。

空间复杂度：O(1)O(1) 或 O(n)O(n)。某些语言字符串不可变，需要 O(n)O(n) 的额外空间。

'''