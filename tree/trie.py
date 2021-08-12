class TrieNode:

    def __init__(self):
        self.end = False
        self.key = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, node=None):
        if node is None:
            node = self.root

        if not word:
            node.end = True
            return
        elif node.key.get(word[0], None) is None:
            node.key[word[0]] = TrieNode()
            self.insert(word[1:], node.key[word[0]])
        else:
            self.insert(word[1:], node.key[word[0]])

    def search(self, word, node=None):
        if node is None:
            node = self.root

        if not word and node.end:
            return True
        elif not word and not node.end:
            return False
        elif node.key.get(word[0], None) is None:
            return False
        else:
            return self.search(word[1:], node.key[word[0]])

    def starts_with(self, word, node=None):
        if node is None:
            node = self.root

        if not word:
            return True
        elif node.key.get(word[0], None) is None:
            return False
        else:
            return self.starts_with(word[1:], node.key[word[0]])


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    # trie.search("dog")
    print(trie.search("app"))
    print(trie.starts_with("app"))
    print(trie.search("apple"))

"""
T: O(L)
S : O(N) or O(L)

"""
