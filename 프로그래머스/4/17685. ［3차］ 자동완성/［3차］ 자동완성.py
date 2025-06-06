class Node:
    def __init__(self):
        self.children = dict()
        self.cnt = 0
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        
        num = 0
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
                
            node = node.children[c]
            node.cnt += 1
            
        node.is_end = True
        
        return num
    
    def count_prefix(self, word):
        node = self.root
        
        cnt = 0
        
        for c in word:
            node = node.children[c]
            cnt += 1
            
            # 여기서부터 유일한 접두어임
            if node.cnt == 1:
                break
                
        return cnt

def solution(words):
    answer = 0
    
    trie = Trie()
    
    for word in words:
        trie.insert(word)
        
    for word in words:
        answer += trie.count_prefix(word)
        
    return answer