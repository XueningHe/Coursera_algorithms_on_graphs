#Uses python3

import sys

def explore(adj,v,visited,result):
    visited[v]=result
    for w in adj[v]:
        if (visited[w]==-1):
            visited=explore(adj,w,visited,result)
    return visited

def number_of_components(adj):
    n=len(adj)
    visited = [-1] * n
    result = 0
    for i in range(n):
        if visited[i]==-1:
            visited=explore(adj,i,visited,result)
            result=result+1
    return result


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
    print(number_of_components(adj))
