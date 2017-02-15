s = "barfoothefoobarman"
words = ["foo", "bar"]

# # You are given a string, s, and a list of words, words,
# # that are all of the same length. Find all starting indices of substring(s)
# # in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# # You should return the indices: [0,9].
# # (order does not matter).
#
#
# Naive approach:
word_length = len(words[0])
words_num = len(words)
start_pos = 0
words_pos = {}
result = []

for pos in range(len(s)):
    this_word = s[pos:(pos + word_length)]
    if this_word in words:
        words_pos[pos] = this_word

# print(words_pos)


for i in sorted(words_pos.keys()):
    temp_list = [(i + word_length*x) for x in range(words_num)]
    if all(j in words_pos for j in temp_list):
        temp_words_lst = [words_pos[k] for k in temp_list]
        if len(temp_words_lst) == len(set(temp_words_lst)):         #wrong because there might be duplicated words
            result.append(i)

print(result)

#
#
# # Version 2
# import collections
#
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# word_length = len(words[0])
# words_num = len(words)
# start_pos = 0
# words_pos = {}
# result = []
#
# for pos in range(len(s)):
#     this_word = s[pos:(pos + word_length)]
#     if this_word in words:
#         words_pos[pos] = this_word
#
# # print(words_pos)
#
#
# for i in sorted(words_pos.keys()):
#     temp_list = [(i + word_length*x) for x in range(words_num)]
#     if all(j in words_pos for j in temp_list):
#         temp_words_lst = [words_pos[k] for k in temp_list]
#         # hash count, O(n); can use sorted(x) == sorted(y), O(nlogn)
#         if collections.Counter(temp_words_lst) == collections.Counter(words):
#             result.append(i)
#
# print(result)
# # Run time error


# Version 3
# since the length of words were all the same, we just need to read a fixed length of string, start at pos 0
# for e.g., words contains 2*3 strings, we need to read 6 length string at one time. so if in this 6 length
# string, the word count is the same as it should be, we just return the first index; else move forward.

word_length = len(words[0])
words_num = len(words)
start_pos = 0
words_count = {}
temp_words_count = {}
result = []
for i in words:
    try:
        words_count[i] += 1
    except:
        words_count[i] = 1

print(words_count)

start_pos = 0
while start_pos <= (len(s) - words_num*word_length):

    break_pos = start_pos + words_num*word_length
    i = start_pos
    print(start_pos, break_pos)
    while i < break_pos:
        this_word = s[i:(i+word_length)]
        print(this_word)
        if this_word in words:
            try:
                temp_words_count[this_word] += 1
            except:
                temp_words_count[this_word] = 1
            if temp_words_count[this_word] > words_count[this_word]:
                temp_words_count = {}
                break
            elif temp_words_count == words_count:
                temp_words_count = {}
                result.append(start_pos)
        else:
            temp_words_count = {}
            break
        i += word_length
    start_pos += 1

print(result)

