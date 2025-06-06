import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        
        node.is_end = True

    def insert_customize(self, word) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            if node.is_end:
                return False

            node = node.children[ch]
        
        node.is_end = True

        if node.children:
            return False

        return True

    def search(self, prefix) -> bool:
        return self._find_node(prefix) is not None
    
    def _find_node(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return None
            
            node = node.children[ch]

        return node
    
    def delete(self, word) -> bool:
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                
                node.is_end = False
                return len(node.children) == 0
            
            ch = word[depth]

            if ch is not node.children:
                return False
            
            should_delete_child = _delete(node.children[ch], word, depth + 1)

            if should_delete_child:
                del node.children[ch]
                return not node.is_end and len(node.children) == 0
            
            return False
        
        return _delete(self.root, word, 0)

T = int(input())

for _ in range(T):
    trie = Trie()

    n = int(input())
    words = [input().strip() for _ in range(n)]

    flag = True

    for word in words:
        flag = flag and trie.insert_customize(word)

    print("YES" if flag else "NO")
