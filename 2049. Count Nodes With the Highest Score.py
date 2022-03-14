'''
There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.

 

Example 1:


Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
Example 2:


Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
 

Constraints:

n == parents.length
2 <= n <= 105
parents[0] == -1
0 <= parents[i] <= n - 1 for i != 0
parents represents a valid binary tree.
通过次数5,554提交次数11,730

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-nodes-with-the-highest-score
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

from typing import *
from collections import *

parents = [-1, 2, 0, 2, 0]


class Node:
    def __init__(self, parent, idx):
        self.parent = parent
        self.children = []
        self.idx = idx
        self.size = 0

    def __repr__(self):
        return f"Node({self.idx} <- parent {self.parent})"

node_dict = {}
from collections import defaultdict
children_dict = defaultdict(list)
cur_node = Node(-1, idx=0)
for idx, parent in enumerate(parents):
    node = Node(parent, idx)
    node_dict[idx] = node
    children_dict[parent].append(idx)


size_dict = {0: len(parents)}

def get_size(n, size_dict):
    if n not in size_dict:
        size_dict[n] = 1
        for c in children_dict.get(n, []):
            size_dict[n] += get_size(c, size_dict)
    return size_dict[n]

max_s = 0
for idx, parent in enumerate(parents):
    if idx == 0: # 根节点
        new_s = 0
        for c in children_dict.get(idx, []):
            new_s += get_size(c, size_dict)
    elif idx not in children_dict: # 叶子节点
        new_s = get_size(0, size_dict) - 1
    else:
        new_s = 1
        for c in children_dict[idx]:
            new_s *= get_size(c, size_dict)
        sibling = [i for i in children_dict[parent] if i != idx]
        for s in sibling:
            new_s *= get_size(s, size_dict) + 1
    max_s = max(max_s, new_s)

max_s


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        pass




parents = [-1,3,3,5,7,6,0,0]

node_dict = {}
from collections import defaultdict
children_dict = defaultdict(list)
for idx, parent in enumerate(parents):
    children_dict[parent].append(idx)

size_dict = {0: len(parents)}

def get_size(n, size_dict):
    if n not in size_dict:
        size_dict[n] = 1
        for c in children_dict.get(n, []):
            size_dict[n] += get_size(c, size_dict)
    return size_dict[n]

max_s = 0
nodes = []
for idx, parent in enumerate(parents):
    if idx == 0: # 根节点
        new_s = 1
        for c in children_dict.get(idx, []):
            new_s *= get_size(c, size_dict)
    elif idx not in children_dict: # 叶子节点
        new_s = get_size(0, size_dict) - 1
    else:
        new_s = 1
        for c in children_dict[idx]:
            new_s *= get_size(c, size_dict)
        new_s *= (get_size(0, size_dict) - get_size(idx, size_dict))
        # sibling = [i for i in children_dict[parent] if i != idx]
        # for s in sibling:
        #     new_s *= get_size(s, size_dict)
        #
    if new_s > max_s:
        nodes = [idx]
        max_s = new_s
    elif new_s == max_s:
        nodes.append(idx)
    print(idx, new_s, max_s, nodes)


print(len(nodes))