'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解法1

from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edge_dict = defaultdict(set)
        for e in edges:
            root, node = e
            edge_dict[root].add(node)
            edge_dict[node].add(root)

        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(edge_dict[i]) == 1)
            s -= leaves

            for l in leaves:
                for j in edge_dict[l]:
                    edge_dict[j].remove(l)
                edge_dict.pop(l)
        return list(s)


# 解法2



from collections import defaultdict
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

edge_dict = defaultdict(set)
for e in edges:
    root, node = e
    edge_dict[root].add(node)
    edge_dict[node].add(root)

