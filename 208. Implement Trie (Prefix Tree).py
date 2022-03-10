'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Trie:

    def __init__(self):
        self.trie_dict = {}

    def insert(self, word: str) -> None:
        node = self.trie_dict
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['end'] = 1

    def search(self, word: str) -> bool:
        node = self.trie_dict
        for w in word:
            if w not in node:
                return False
            node = node[w]
        if 'end' in node:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        node = self.trie_dict
        for w in prefix:
            if w not in node:
                return False
            node = node[w]
        return True



    def startsWith(self, prefix: str) -> bool:
        node = self.trie_dict
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return True


word = 'test'
trie_dict = {}

trie = Trie()
trie.insert('test')
trie.search('test2')
trie.search('tes')
trie.search('test')