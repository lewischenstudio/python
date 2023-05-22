"""
Trie
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("Successfully inserted")

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node is None:
                return False
            currentNode = node

        if currentNode.endOfString:
            return True
        else:
            return False

    def deleteString(self, root, word, index):
        ch = word[index]
        currentNode = root.children.get(ch)
        canThisNodeBeDeleted = False
        print("currentNode.children: ", len(currentNode.children))
        if len(currentNode.children) > 1:
            self.deleteString(currentNode, word, index + 1)
            return False

        if index == len(word) - 1:
            if len(currentNode.children) >= 1:
                currentNode.endOfString = False
                return False
            else:
                root.children.pop(ch)
                return True

        if currentNode.endOfString:
            self.deleteString(currentNode, word, index + 1)
            return False

        canThisNodeBeDeleted = self.deleteString(currentNode, word, index + 1)
        if canThisNodeBeDeleted:
            root.children.pop(ch)
            return True
        else:
            return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))
print(newTrie.searchString("Appl"))
newTrie.deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("Appl"))
