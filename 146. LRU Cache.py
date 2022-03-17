'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Node:
    def __init__(self, parent, child, key, val):
        self.parent = parent
        if isinstance(self.parent, Node):
            self.parent.child = self
        self.child = child
        self.key = key
        self.val = val

    def __repr__(self):
        return f"node({self.key})"


class LRUCache:

    def __init__(self, capacity: int):
        self.root = Node(parent=None, child=None, key='root', val='root')
        self.leaf = Node(parent=self.root, child=None, key='root', val='end')
        self.key2node = {'root':self.root, 'leaf':self.leaf}
        self.capacity = capacity

    def use(self, node):
        # 断开原来的链条
        # 对于儿子：
        if isinstance(node.child, Node):
            node.child.parent = node.parent
        # 对于父亲：
        if isinstance(node.parent, Node):
            node.parent.child = node.child
        # 原来第一个节点
        curr_first_node = self.root.child
        if curr_first_node != node:
            curr_first_node.parent = node
            node.child = curr_first_node
        # 根节点
            self.root.child = node
            node.parent = self.root
        self._print()


    def evict(self):
        self._print()
        node2evict = self.leaf.parent
        node2evict.parent.child = self.leaf
        self.leaf.parent = node2evict.parent
        print("evict!")
        self.key2node.pop(node2evict.key)
        self._print()


    def get(self, key: int) -> int:
        node = self.key2node.get(key, None)
        if node is None:
            if key in self.key2node:
                self.key2node.pop(key)
            return -1
        else:
            self.use(node)
            return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.key2node:
            node = Node(parent=None, child=None, key=key, val=value)
            self.key2node[key] = node
        else:
            node = self.key2node[key]
            node.val = value
        self.use(node)
        if len(self.key2node) > self.capacity + 2:
            self.evict()

    def _print(self):
        i = self.root
        while i != self.leaf:
            print(f'{i}->', end="")
            i = i.child
        print(i)
        pass


self = LRUCache(2)
self.put(1, 1)
self.put(2, 2)
self.get(1)
self.put(3, 3)
self.get(2)
self.put(4, 4)
self.get(1)
self.get(3)
self.get(4)





# 标准解法
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
