'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''

'''
Thought:
x[0] = 1
x[1] = 11

x[2] =  ...

My solution: define a function to return the next
'''

def find_count(input_str):
    output = ''
    count = 1
    for pos in range(1, len(input_str)):
        if input_str[pos] == input_str[pos-1]:
            count += 1
        else:
            output += '{count}{string}'.format(count=count, string=input_str[pos-1])
            count = 1
    output += '{count}{string}'.format(count=count, string=input_str[-1])
    return output

def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if not n:
        return ""
    elif n==1:
        return 1
    else:
        start = 2
        next = '11'
        while start < n:
            next = find_count(next)
            start += 1
        return next

