#Uses python3

import sys
import queue

def bipartite_CC(adj,v,col):
    n = len(adj)
    col[v]=1
    queue=[v]
    while len(queue)>0:
        u=queue.pop(0)
        for v in adj[u]:
            if col[v]==col[u]:
                return False,col
            if col[v]==0:
                queue.append(v)
                col[v]=col[u]*(-1)
    return True,col
    
def bipartite(adj):
    n = len(adj)
    col=[0] * n
    for i in range(n):
        if col[i]==0:
            boo,col=bipartite_CC(adj,i,col)
            if not boo:
                return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
