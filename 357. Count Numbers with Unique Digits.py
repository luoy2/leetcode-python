'''
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1
 

Constraints:

0 <= n <= 8
通过次数34,341提交次数62,622

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''





import operator as op
from functools import reduce


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        curr, res = 1, 10
        while curr < n:
            res += 9 * reduce(op.mul, range(9, 9 - curr, -1), 1)
            curr += 1
        return res
