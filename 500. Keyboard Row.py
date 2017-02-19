# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
words = ["Hello", "Alaska", "Dad", "Peace"]

# My solution:
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = [i for i in 'qwertyuiopQWERTYUIOP']
        row2 = [i for i in 'asdfghjklASDFGHJKL']
        row3 = [i for i in 'zxcvbnmZXCVBNM']
        result_lst = []
        for word in words:
            if set(word).intersection(set(row1)) == set(word):
                result_lst.append(word)
            elif set(word).intersection(set(row2)) == set(word):
                result_lst.append(word)
            elif set(word).intersection(set(row3)) == set(word):
                result_lst.append(word)
        return result_lst

# one line python:
def findWords(words):
    return [word for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')] for word in words if
            set(word.lower()) <= row]

# set([2,3]) <= set([2,3, 4]) means set 1 belongs to set 2