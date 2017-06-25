'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

'''
my solution:
loop through the string, and record all the open bracket; if there is a close one,
check if last open bracket equals this close one. if not return False; if there is no open
bracket, return false; if it is, remove the last element of open_list


After loop, check if open list is empty.
'''

class Solution(object):
    def isValid(self, s):
        open = ['(', '{', '[']
        close = [')', '}', ']']
        order_dict = {i:v for i,v in zip(open, close)}
        open_list = []
        if len(s) <= 1:
            return False
        result = True
        for i in s:
            if i in open:
                open_list.append(i)
            elif i in close:
                if not open_list:
                    return False
                elif order_dict[open_list[-1]] != i:
                    return False
                else:
                    open_list = open_list[:-1]
            else:
                pass
        if open_list:
            return False
        return True

# pythonic solution:
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []