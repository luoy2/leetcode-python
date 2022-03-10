'''
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/base-7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 10进制转换N进制： 整除base, 逆序排余。

class Solution:
    def convertToBase7(self, num: int) -> str:
        div = 1
        base = 7
        result = ''
        is_neg = False
        if num < 0:
            is_neg = True
            num = -1 * num
        while div != 0:
            div = num // base
            mod = num % base
            # print(num, div, mod)
            result = str(mod) + result
            num = div
        if is_neg:
            result = '-' + result
        return result