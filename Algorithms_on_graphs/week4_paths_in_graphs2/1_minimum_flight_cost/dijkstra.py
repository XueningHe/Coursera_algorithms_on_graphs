#Uses python3

import sys
import queue
import math


def extract_min(H,Q):
    min_dist=H[Q[0]]
    min_vertex=Q[0]
    for v in Q:
        if H[v]<min_dist:
            min_dist=H[v]
            min_vertex=v
    return min_vertex,min_dist


def distance(adj, cost, s, t):
    n=len(adj)
    H=[math.inf] * n
    if t>n:
        return -1
    H[s]=0
    Q=list(range(n))
    while len(Q)>0:
        u,dist_u=extract_min(H,Q)
        Q.remove(u)
        costs_from_u=cost[u]
        for i in range(len(adj[u])):
            v=adj[u][i]
            if H[v]>H[u]+costs_from_u[i]:
                H[v]=H[u]+costs_from_u[i]
    if math.isinf(H[t]):
        return -1
    return H[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
