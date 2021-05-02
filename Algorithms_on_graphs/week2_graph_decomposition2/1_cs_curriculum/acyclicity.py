#Uses python3

import sys

def isCyclic(adj, v):
    global cur_path,visited
    cur_path.add(v)
    for w in adj[v]:
        if w in cur_path:
            return 1
        else:
            if isCyclic(adj, w):
                return 1
    cur_path.remove(v)
    return 0

def acyclic(adj):
    global visited,cur_path
    n=len(adj)
    cur_path = set()
    visited = [0] * n
    for i in range(n):
        if visited[i]==0:
            cur_path = set()
            if isCyclic(adj,i):
                return 1
    return 0
        

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
