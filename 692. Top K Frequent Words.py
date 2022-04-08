'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Word:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):  # True: self比other先淘汰
        if self.cnt > other.cnt:  # freq小的先弹出
            return False
        elif self.cnt < other.cnt:
            return True
        else:
            return self.word > other.word  # 字典序大的先弹出


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # time: nlogn
        # space: n
        q = []
        freq = collections.Counter(words)
        for word, cnt in freq.items():
            heapq.heappush(q, Word(word, cnt))
            if len(q) > k:
                heapq.heappop(q)
        res = []
        while q:
            res.append(heapq.heappop(q).word)  # 先弹出的是频率较小的，结果要逆序
        return res[::-1]