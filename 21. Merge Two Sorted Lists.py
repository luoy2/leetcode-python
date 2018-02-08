'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import time

class Solution:
    def mergeTwoLists(self, list1, list2):
        output_list = []
        while list1 or list2:
            try:
                print(list1.val, list2.val, output_list)
                if list1.val <= list2.val:
                    output_list.append(list1.val)
                    list1 = list1.next
                else:
                    output_list.append(list2.val)
                    list2 = list2.next
            except AttributeError:
                remain_list = list1 if list1 else list2
                while remain_list:
                    output_list.append(remain_list.val)
                    remain_list = remain_list.next
                list1 = None
                list2 = None
        return output_list




# Recursive solution
def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a


'''

a : 1 -> 4 -> None
b : 2 -> 3 -> None


first :
a.next    a: 1 - >()

merge(4->None, 2->3->None)

    a: 2->3->None
    b: 4-> None
    a.next(3->None, 4->NONE)   : 
    
        a: 3 -> merge(None, 4->None)


'''