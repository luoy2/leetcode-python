# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space
# (size that is greater or equal to m + n) to hold additional elements from nums2.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
nums1 = [1,2,3,4]
nums2 = [0,2,3,4]


nums1 = [0, 0, 0, 1, 2]
nums2 = [2, 3]
"""
:type nums1: List[int]
:type m: int
:type nums2: List[int]
:type n: int
:rtype: void Do not return anything, modify nums1 in-place instead.
"""
nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
nums2 = [-1,-1,0,0,1,2]
m=5
n=6
"""
:type nums1: List[int]
:type m: int
:type nums2: List[int]
:type n: int
:rtype: void Do not return anything, modify nums1 in-place instead.
"""
"""
:type nums1: List[int]
:type m: int
:type nums2: List[int]
:type n: int
:rtype: void Do not return anything, modify nums1 in-place instead.
"""

# Naive Approach:
# Start iterate from the very begining, and insert element from nums2 into nums1
if m == 0 and n == 0:
    print([])
elif m == 0:
    nums1[:] = nums2
    print(nums1)
elif n == 0:
    print(nums1)
else:
    pos1 = 0
    pos2 = 0
    while pos1 <= len(nums1):
        print(pos1,pos2)
        print(nums1)
        print(nums2)
        if pos1 >= m and nums1[pos1] == 0:
            print('aaa', pos1, pos2)
            nums1[pos1:(pos1 + len(nums2) - pos2)] = nums2[pos2:len(nums2)]
            break
        if pos2 == n:
            break
        if nums2[pos2] < nums1[pos1]:
            nums1[(pos1 + 1):] = nums1[pos1:(len(nums1) - 1)]
            nums1[pos1] = nums2[pos2]
            m+=1
            pos1 += 1
            pos2 += 1
        else:
            pos1 += 1
    print(nums1)