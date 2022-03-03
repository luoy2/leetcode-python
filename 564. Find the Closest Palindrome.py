'''
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 

Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-closest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

n = "1213"
def get_palindromic(n: str) -> str:
    top = len(n) // 2
    is_odd = len(n) % 2
    if is_odd:
        reconstruct = n[:top] + n[top] + n[:top][::-1]
    else:
        reconstruct = n[:top] + n[:top][::-1]
    return reconstruct

def get_nearest_palindromic(n: str):
    top = len(n) // 2
    is_odd = len(n) % 2
    reconstruct = get_palindromic(n)
    reconstruct_int = int(reconstruct)
    subs = str(reconstruct_int - 10 ** int(len(n) - top - 1 * is_odd))
    adds = str(reconstruct_int + 10 ** int(len(n) - top - 1 * is_odd))
    candidates = []
    for cand in [subs, adds]:
        print(cand)
        if len(cand) != len(n):
            top = len(cand) // 2
            is_odd = len(cand) % 2
            if len(cand) < len(n):
                reconstruct_2 =  '9'*len(cand)
                candidates.append(reconstruct_2)
                continue
        if is_odd:
            reconstruct_2 = cand[:top] + cand[top] +cand[:top][::-1]
        else:
            reconstruct_2 = cand[:top] + cand[:top][::-1]
        candidates.append(reconstruct_2)
    return candidates

def nearestPalindromic(n:str):
    if len(n) == 1:
        return str(int(n) - 1)
    near_palindromic = get_palindromic(n)
    small_palindromic, large_palindromic = get_nearest_palindromic(n)
    print("candidates:", near_palindromic, small_palindromic, large_palindromic)
    int_n = int(n)
    distances = []
    for cand in large_palindromic, near_palindromic, small_palindromic:
        distances.append(abs(int(cand) - int_n))
    best = ''
    smallest_dist = 1e9
    for d, r in zip(distances, (large_palindromic, near_palindromic, small_palindromic)):
        print(d, r)
        if d != 0 and d <= smallest_dist:
            best = r
            smallest_dist = d
    print(best)
    return best
nearestPalindromic("1805170081")
