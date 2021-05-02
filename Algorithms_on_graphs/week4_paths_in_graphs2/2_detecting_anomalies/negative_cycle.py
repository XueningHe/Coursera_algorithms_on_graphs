#Uses python3

import sys
import math

def Bellman_Ford_CC(edges,adj,dist,s):
    n=len(adj)
    dist[s]=0
    for times in range(n-1):
        for u,v,w in edges:
            if dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
    changed=[]
    for u,v,w in edges:
        if dist[v]>dist[u]+w:
            dist[v]=dist[u]+w
            changed.append(v)
    if len(changed)==0:
        return dist,False
    return dist,True
    
            
    
def negative_cycle(adj,cost):
    n=len(adj)
    dist=[math.inf]*n
    edges=[]
    for i in range(n):
        if len(adj[i])>0:
            for idx in range(len(adj[i])):
                edges.append((i,adj[i][idx],cost[i][idx]))
    while math.inf in dist:
        s=dist.index(math.inf)
        dist,is_nwc=Bellman_Ford_CC(edges,adj,dist,s)
        if is_nwc:
            return 1
    return 0
   


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
