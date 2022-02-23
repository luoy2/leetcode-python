'''
You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 6
Explanation: The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.
Example 2:

Input: nums = [4,2,3,15]
Output: 5
Explanation: The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-number-of-good-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import cProfile
import pstats
from pstats import SortKey

from itertools import combinations
import math




'''
[6,8,1,8,6,5,6,11,17]  62
[9,3,14,12,14,3,23,23,30,9,2,6,26,17,5,8,23,6,8,9,2,4,30,21,19,8,1,23,22,26,17,20,5,15,18,20,22,2,15,8,21,9,20] 9958
[20,21,12,7,30,8,27,5,23,7,12,5,29,21,6,26,11,19,7,6,3,10,20,6,14,10,27,21,19,5,8,7,3,1,1,23,27,20,10,3,16,18,20,21,27,12,19,10,10,13,12,25,5,21,29,21,17,5,7,22,22,21,2,18,22,17,4,25,3,6,20,4,16,15,16,14,20,1,8,4,10,16,29,8,21,30,13,20,7,3,5,19,14,10,8]

'''
nums = [20, 21, 12, 7, 30, 8, 27, 5, 23, 7, 12, 5, 29, 21, 6, 26, 11, 19, 7, 6, 3, 10, 20, 6, 14, 10, 27, 21, 19, 5, 8,
        7, 3, 1, 1, 23, 27, 20, 10, 3, 16, 18, 20, 21, 27, 12, 19, 10, 10, 13, 12, 25, 5, 21, 29, 21, 17, 5, 7, 22, 22,
        21, 2, 18, 22, 17, 4, 25, 3, 6, 20, 4, 16, 15, 16, 14, 20, 1, 8, 4, 10, 16, 29, 8, 21, 30, 13, 20, 7, 3, 5, 19,
        14, 10, 8]

class Solution(object):
    def numberOfGoodSubsets(self, nums):
        good_list = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        prime_count = {}
        set_count = {}
        one_count = 0
        for n in nums:
            if n == 1:
                one_count += 1
            elif n in good_list:
                prime_count[n] = prime_count.get(n, 0) + 1
                set_count[n] = 1
        prev_candidates_list = [frozenset((i,)) for i in prime_count]
        print(prev_candidates_list)
        all_candidates = set(prev_candidates_list)

        def prune(item, cands):
            for i in combinations(item, len(item) - 1):
                if frozenset(i) not in cands:
                    return False
            return True

        def generate_n_item_candidates(prev_candidates_list, set_count, all_cands):
            if not prev_candidates_list:
                return [], set_count
            res = {}
            target_length = len(prev_candidates_list[0]) + 1
            for i in combinations(prev_candidates_list, 2):
                merged = i[0].union(i[1])
                # print(merged)
                if len(merged) == target_length:
                    # print(merged)
                    if prune(merged, all_cands):
                        # print(merged)
                        res[merged] = 0
            for k, v in res.items():
                for m in k:
                    set_count[m] += 1
            result = list(res.keys())
            # print(result)
            return result, set_count

        total = len(prev_candidates_list)
        next_item_candidates = []
        for i, j in combinations(prime_count, 2):
            if math.gcd(i, j) == 1:
                set_count[i] += 1
                set_count[j] += 1
                next_item_candidates.append(frozenset([i, j]))
        all_candidates = all_candidates.union(next_item_candidates)
        # print(next_item_candidates)
        total += len(next_item_candidates)
        item_set_length = 3
        while next_item_candidates:
            print(f"mining itemset length {item_set_length}...")
            next_item_candidates, set_count = generate_n_item_candidates(next_item_candidates, set_count, all_candidates)
            all_candidates = all_candidates.union(next_item_candidates)
            # print(next_item_candidates)
            total += len(next_item_candidates)
            item_set_length += 1

        all_total = 0
        for c in all_candidates:
            this_comb = 1
            for n in c:
                this_comb *= prime_count[n]
            all_total += this_comb
        all_total *= pow(2, one_count)
        print(all_total)
        return all_total % (10 ** 9 + 7)



self = Solution()
self.numberOfGoodSubsets(nums)
# cProfile.run("self.numberOfGoodSubsets(nums)", 'cstats')
# p = pstats.Stats('cstats')
# p.sort_stats(SortKey.CUMULATIVE).print_stats(20)


# 优化：
from collections import Counter, defaultdict
class Solution(object):
    def numberOfGoodSubsets(self, nums) -> int:
        ct, mod = Counter(nums), 10**9+7
        d = defaultdict(int)
        d[1] = (1 << ct[1]) % mod
        for num in [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]:
            for x in list(d):
                if math.gcd(num, x) == 1:
                    d[num*x] += ct[num]*d[x]
                    d[num*x] %= mod
        return (sum(d.values())-d[1]) % mod