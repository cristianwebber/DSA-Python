from __future__ import annotations


class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.counter = 0
        self.children = {}


class Trie():
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character
        # or create a new child for the current node

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_word = True
        node.counter += 1

    def dfs(self, node: TrieNode, prefix: str):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_word:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x: str) -> list[tuple[str, int]]:
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output: list[tuple[str, int]] = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)


def test_trie():
    t = Trie()
    t.insert('was')
    t.insert('word')
    t.insert('work')
    t.insert('war')
    t.insert('what')
    t.insert('where')
    t.insert('where')
    t.insert('where')
    assert t.query('wor') == [('word', 1), ('work', 1)]
    assert t.query('wh') == [('where', 3), ('what', 1)]
