class DisjointSet:
    def _init_(self, n):
        self.parent = list(range(n+1))
        
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
        
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False
def kruskal_mst(n, edges):
    edges.sort(key = lambda x: x[2])
    ds = DisjointSet(n)
    mst_weight = 0
    for u,v,w in edges:
        if ds.union(u,v):
            mst_weight += w
    return mst_weight
    
    
T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    edges = []
    for _ in range(M):
        u,v,w = map(int,input().split())
        edges.append((u,v,w))
    print(kruskal_mst(N,edges))
