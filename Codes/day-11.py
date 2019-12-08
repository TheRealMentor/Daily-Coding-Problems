#Without trie data structure
def autocomplete(s):
    data = ['dog', 'deer', 'deal']
    l = len(s)
    res = []

    for word in data:
        if word[:l] == s:
            res.append(word)
    
    return res

print(autocomplete('de'))

#With Trie data structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []
    
    def formTrie(self, keys):
        for key in keys:
            self.insert(key)
    
    def insert(self, key):
        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()
            node = node.children[a]
        
        node.isLast = True
    
    def search(self, key):
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            
            node = node.children[a]
        
        return node and node.isLast and found
    
    def suggestRec(self, node, word):
        if node.isLast:
            self.word_list.append(word)
        
        for a, n in node.children.items():
            self.suggestRec(n, word+a)
    
    def autocomplete(self, key):
        node = self.root

        not_found = False
        tmp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
            tmp_word += a        
            node = node.children[a]
        
        if not_found:
            return 0
        elif node.isLast and not node.children:
            return -1
        
        self.suggestRec(node, tmp_word)

        for s in self.word_list:
            print(s)
        return 1
    
keys = ["hello", "dog", "hell", "cat", "a", "hel", "help", "helps", "helping"]
key = 'help'

t = Trie()
t.formTrie(keys)

ans = t.autocomplete(key)

if ans == -1:
    print('No other strings found!')
elif ans == 0:
    print('No string found!')
