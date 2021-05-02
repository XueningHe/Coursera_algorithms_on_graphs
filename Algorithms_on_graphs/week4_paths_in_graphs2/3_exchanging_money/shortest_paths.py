#Uses python3

import sys
import math
def Bellman_Ford(adj,cost,s):
    n=len(adj)
    dist=[math.inf]*n
    dist[s]=0
    prev=[math.inf]*n
    edges=[]
    for i in range(n):
        if len(adj[i])>0:
            for idx in range(len(adj[i])):
                edges.append((i,adj[i][idx],cost[i][idx]))
    for times in range(n-1):
        for u,v,w in edges:
            if dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
                prev[v]=u                
    changed=[]
    for u,v,w in edges:
        if dist[v]>dist[u]+w:
            dist[v]=dist[u]+w
            prev[v]=u 
            changed.append(v)
    return dist,changed,prev
                 
def reachable_from_cycle(adj,cycle):
    n = len(adj)
    visited=[False] * n
    visited[cycle[0]]=True
    queue=[v for v in cycle]
    while len(queue)>0:
        u=queue.pop(0)
        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v]=True
    reachable_vs=[]
    for i in range(len(visited)):
        if visited[i]:
            reachable_vs.append(i)
    return reachable_vs


def locate_cycle(prev,v):
    n=len(prev)
    for i in range(n):
        v=prev[v]
    path=[]
    while v not in path:
        path.append(v)
        v=prev[v]
    return path
    
    

def shortet_paths(adj, cost, s, reachable, shortest):
    dist,changed,prev=Bellman_Ford(adj,cost,s)
    for i in range(len(adj)):
        if not math.isinf(dist[i]):
            reachable[i]=1
    if len(changed)==0:
        return reachable,shortest,dist
    
    cycle=locate_cycle(prev,changed[0])
    vs=reachable_from_cycle(adj,cycle)
    for v in vs:
        shortest[v]=0
    return reachable,shortest,dist
        
    
    


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
    s = data[0]
    s -= 1
    reachable = [0] * n
    shortest = [1] * n
    reachable,shortest,distance = shortet_paths(adj, cost, s, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

