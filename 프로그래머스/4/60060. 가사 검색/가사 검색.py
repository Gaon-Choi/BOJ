from collections import defaultdict

class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
                
            node.cnt += 1
            
            node = node.children[c]
            
        node.is_end = True
        
    def find(self, prefix: str) -> int:
        node = self.root
        
        for c in prefix:
            if c not in node.children:
                return 0
            
            node = node.children[c]
            
        return node.cnt

def solution(words, queries):
    answer = []
    
    prefix_arr = defaultdict(Trie)
    postfix_arr = defaultdict(Trie)
    
    for word in words:
        prefix_arr[len(word)].insert(word)
        postfix_arr[len(word)].insert(word[-1::-1])
    
    for q in queries:
        is_postfix = False
        if q[0] == "?":
            is_postfix = True
            
        temp = ""
        
        for c in q:
            if c != "?":
                temp += c
                
        if is_postfix:
            temp = temp[-1::-1]
            answer.append(postfix_arr[len(q)].find(temp))
        else:
            answer.append(prefix_arr[len(q)].find(temp))
            
    return answer
    