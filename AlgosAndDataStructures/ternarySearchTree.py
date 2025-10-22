"""
Ternary search tree

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.ends_here = False  # if you find a word here
        self.left = None  # every node as three children
        self.right = None
        self.eq = None


class TernarySearchTree:

    def __init__(self):
        self.root = None

    def _insert_util(self, node, word, i):
        if i == len(word):
            return node

        if node is None:
            node = Node(word[i])

        if ord(word[i]) < ord(node.data):
            node.left = self._insert_util(node.left, word, i)

        elif ord(word[i]) > ord(node.data):
            node.right = self._insert_util(node.right, word, i)

        else:
            node.eq = self._insert_util(node.eq, word, i + 1)

            if i == len(word) - 1:
                node.ends_here = True

        return node

    def insert(self, word):
        self.root = self._insert_util(self.root, word, 0)

    def _search_util(self, node, word, i):
        if i == len(word):
            return True

        if node is None:
            return False

        if ord(word[i]) < ord(node.data):
            return self._search_util(node.left, word, i)

        elif ord(word[i]) > ord(node.data):
            return self._search_util(node.right, word, i)
        else:
            exists = self._search_util(node.eq, word, i + 1)
            if exists:
                if i == len(word) - 1 and node.ends_here is False:
                    return False
                return True

        return False

    def search(self, word) -> bool:
        return self._search_util(self.root, word, 0)

    def _find_all_util(self, node, words, word):
        # print(node, words, word)
        if node is None:
            return

        # include
        self._find_all_util(node.eq, words, word + node.data)

        # exclude
        self._find_all_util(node.left, words, word)
        self._find_all_util(node.right, words, word)

        if node.ends_here is True:
            words.append(word + node.data)

    def find_all(self):
        words = []
        self._find_all_util(self.root, words, "")
        return words


if __name__ == '__main__':
    tst = TernarySearchTree()

    tst.insert("call")
    tst.insert("me")
    tst.insert("mind")
    tst.insert("mid")

    # print(tst.root)

    print("#########")
    print("mid: ", tst.search("mid"))
    print("mind: ", tst.search("mind"))
    print("cme: ", tst.search("cme"))
    print("cal: ", tst.search("cal"))
    print("me: ", tst.search("me"))

    print("#########")
    print("all words:", tst.find_all())
