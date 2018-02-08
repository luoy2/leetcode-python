'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

#import time
s = "cbaebabacd"
p = "abc"

start = 0
end = len(p)

s_dict = {i: s[:end].count(i) for i in set(s) if s[:end].count(i)}
p_dict = {i:p.count(i) for i in set(p)}

output_index = []
while end <= len(s):
    #print(s[start:end], s_dict, p_dict, output_index)
    if s_dict == p_dict:
        output_index.append(start)
    s_dict[s[start]] -= 1
    if not s_dict[s[start]]:
        del s_dict[s[start]]
    try:
        s_dict[s[end]] += 1
    except KeyError:
        s_dict[s[end]] = 1
    except IndexError:
        break
    start += 1
    end += 1
    # time.sleep(1)
print(output_index)
