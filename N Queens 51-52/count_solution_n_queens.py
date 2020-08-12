class Solution:
    def totalNQueens(self, n: int) -> int:
        self.p = []
        self.count = 0
        
        def no_backtrack():
            i = len(self.p)-1
            for j in range(i):
                if i-j == abs(self.p[i] - self.p[j]):
                    return False
            return True
        
        def findSol(n):
            if len(self.p)==n:
                self.count=self.count+1
                return
            for k in range(n):
                if k not in self.p:
                    self.p.append(k)
                    if no_backtrack():
                        findSol(n)
                    self.p.pop()
        findSol(n)
        return self.count
        
