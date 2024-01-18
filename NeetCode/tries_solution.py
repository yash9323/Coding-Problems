# Neet Code Tries 

class Node:
    def __init__(self):
        self.n = {}
        self.e = False

# 208 Implement Prefix Trie
class Trie:
    def __init__(self):
        self.r = Node()
    def insert(self, word: str) -> None:
        c = self.r 
        for w in word:
            if w not in c.n:
                c.n[w] = Node()
            c = c.n[w]
        c.e = True 
    def search(self, word: str) -> bool:
        c = self.r
        for w in word:
            if w not in c.n:
                return False
            c = c.n[w]
        return c.e 
    def startsWith(self, prefix: str) -> bool:
        c = self.r
        for w in prefix:
            if w not in c.n:
                return False
            c = c.n[w]
        return True
    
# 211 Design Add and Search Words Data Structure 
class WordDictionary:
    def __init__(self):
        self.r = Node()
    def addWord(self, word: str) -> None:
        c = self.r
        for w in word:
            if w not in c.n:
                c.n[w] = Node()
            c = c.n[w]
        c.e = True
    def search(self, word: str) -> bool:
        def f(r,i):
            c = r 
            while i < len(word):
                x = word[i]
                if x == ".":
                    for n in c.n.values():
                        if f(n,i+1):
                            return True 
                    return False
                else:
                    if x not in c.n:
                        return False
                    c = c.n[x]
                i += 1 
            return c.e
        return f(self.r,0)
    
# 212 Word Search 2
def findWords(board, words):
    rr = len(board)
    cc = len(board[0])
    r = {}
    def f(i,j,path,rr):
        w = board[i][j]
        if w in rr.n:
            rr = rr.n[w]
        else:
            return 
        path = path + [w]
        board[i][j] = None
        if rr.e:
            r[''.join(path)] = 1
        if j + 1 < cc: f(i,j+1,path,rr)
        if j - 1 >= 0: f(i,j-1,path,rr)
        if i + 1 < rr: f(i+1,j,path,rr)
        if i - 1 >= 0: f(i-1,j,path,rr)
        board[i][j] = w
    t = Trie()
    for word in words:
        t.insert(word)
    for row in range(rr):
        for col in range(cc):
            f(row,col,[],t.r)
    return r.keys()