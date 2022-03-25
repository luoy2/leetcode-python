'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 朴素解法
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        res = str(math.factorial(n))
        i = -1
        while res[i] == '0':
            cnt += 1
            i -= 1

        return cnt


def trailingZeroes(n: int) -> int:
    cnt = 0
    res = str(math.factorial(n))
    i = -1
    while res[i] == '0':
        cnt += 1
        i -= 1

    return cnt


# 解法 数5

def x(n):
    return trailingZeroes(n) - trailingZeroes(n-1)

n = 625
add = 0
base = 5
new_add = 0
multiplier = 1
zero_dict = {0: 0, 5: 1}
cnt = 0
curr = 0
while curr <= n:
    curr = base * multiplier
    new_add = zero_dict[base] + zero_dict.get(multiplier, 0)
    zero_dict[curr] = new_add
    multiplier += 1
    print(zero_dict)
    cnt += new_add
cnt -= new_add
print(cnt)
trailingZeroes(625)


'''
方法一：数学
n!n! 尾零的数量即为 n!n! 中因子 1010 的个数，而 10=2\times 510=2×5，因此转换成求 n!n! 中质因子 22 的个数和质因子 55 的个数的较小值。

由于质因子 55 的个数不会大于质因子 22 的个数（具体证明见方法二），我们可以仅考虑质因子 55 的个数。

而 n!n! 中质因子 55 的个数等于 [1,n][1,n] 的每个数的质因子 55 的个数之和，我们可以通过遍历 [1,n][1,n] 的所有 55 的倍数求出。

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/jie-cheng-hou-de-ling-by-leetcode-soluti-1egk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


#最优

'''
对于一个数的阶乘，就如之前分析的，5 的因子一定是每隔 5 个数出现一次，也就是下边的样子。

n! = 1 * 2 * 3 * 4 * (1 * 5) * ... * (2 * 5) * ... * (3 * 5) *... * n

因为每隔 5 个数出现一个 5，所以计算出现了多少个 5，我们只需要用 n/5 就可以算出来。

但还没有结束，继续分析。

... * (1 * 5) * ... * (1 * 5 * 5) * ... * (2 * 5 * 5) * ... * (3 * 5 * 5) * ... * n

每隔 25 个数字，出现的是两个 5，所以除了每隔 5 个数算作一个 5，每隔 25 个数，还需要多算一个 5。

也就是我们需要再加上 n / 25 个 5。

同理我们还会发现每隔 5 * 5 * 5 = 125 个数字，会出现 3 个 5，所以我们还需要再加上 n / 125 。

综上，规律就是每隔 5 个数，出现一个 5，每隔 25 个数，出现 2 个 5，每隔 125 个数，出现 3 个 5... 以此类推。

最终 5 的个数就是 n / 5 + n / 25 + n / 125 ...

写程序的话，如果直接按照上边的式子计算，分母可能会造成溢出。所以算 n / 25 的时候，我们先把 n 更新，n = n / 5，然后再计算 n / 5 即可。后边的同理。

作者：windliang
链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        # 第一步， 计算 有多少个5；对于每个5，肯定都有1个2， 那么就能分解出10； 也就是说可以直接+
        # 计算有多少个25； 对于每个25，都可以让cnt +2； 但是由于前面我们已经计算了n/5，这里面包含了所有的25一次， 那么直接+1就行
        # 计算125
        # 。。。。
        # 结束
        while n:
            n //= 5
            ans += n
        return ans


'''
5: 1
25: 6 (5+1)
125 31 (25+6)
'''
