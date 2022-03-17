'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import defaultdict


class Trie:
    def __init__(self):
        self.dict = defaultdict(dict)

    def insert(self, word):
        curr = self.dict
        word_len = len(word)
        has_before = True
        for i, w in enumerate(word):
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
            if 'end' not in curr and i < word_len - 1:
                has_before = False
        curr['end'] = 1
        return has_before

    def isin(self, word):
        curr = self.dict
        for w in word:
            if w in curr:
                curr = curr[w]
            else:
                return False
        if 'end' in curr:
            return True
        else:
            return False

words = ["a","banana","app","appl","ap","apply","apple"]
sorted_word = sorted(words)
print(sorted_word)
max_len = 0
trie = Trie()
result = ''
for w in sorted_word:
    word_len = len(w)
    already_in = trie.insert(w)
    print(w, already_in)
    if already_in and word_len > max_len:
        result = w
        max_len = word_len
print(result)



# 上面需要对nums做sorted， 复杂度是O(N+NlogN). 下面这个简化版只需对result做sort
from collections import defaultdict

class Trie:
    def __init__(self):
        self.dict = {}

    def insert(self, word):
        curr = self.dict
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def real_in(self, word):
        curr = self.dict
        has_before = True
        for w in word:
            curr = curr[w]
            if '#' not in curr:
                has_before = False
        return has_before


words = ["w","wo","wor","worl","world"]
max_len = 0
trie = Trie()
results = ['']
for w in words:
    trie.insert(w)

for w in words:
    word_len = len(w)
    if trie.real_in(w):
        if word_len > max_len:
            results = [w]
            max_len = word_len
        elif word_len == max_len:
            results.append(w)

sorted(results)[0]


# 使用循环+动态规划思想
# sort过后，只有
class Solution:
    def longestWord(self, words: List[str]) -> str:
        max_len = 0
        s_words = sorted(words)
        prefix_set = set()
        result = ''
        for s in s_words:
            is_qualified = False
            word_len = len(s)
            if word_len == 1:
                is_qualified = True
                prefix_set.add(s)
            else:
                if s[:-1] in prefix_set:
                    prefix_set.add(s)
                    is_qualified = True
            if is_qualified:
                if word_len > max_len:
                    result = s
                    max_len = word_len
        return result

# 优化解法

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set, longest_word = set(['']), ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

