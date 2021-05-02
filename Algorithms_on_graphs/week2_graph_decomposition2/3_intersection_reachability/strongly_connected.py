#Uses python3

import sys

sys.setrecursionlimit(20000)

def explore(adj,v,visited):
    global postorder,counter
    visited[v]=1
    counter=counter+1
    for w in adj[v]:
        if visited[w]==0:
            visited=explore(adj,w,visited)
    counter=counter+1
    postorder[v]=counter
    return visited
    
def dfs(adj):
    global postorder
    global counter
    n=len(adj)
    postorder=[-1]*n
    counter=0
    visited=[0]*n
    for i in range(n):
        if visited[i]==0:
            visited=explore(adj,i,visited)
    return postorder

def number_of_strongly_connected_components(adj,adjr):
    postorder=dfs(adjr)
    n=len(adj)
    temp=list(zip(list(range(n)),postorder))
    temp.sort(key=lambda x: x[1],reverse=True)
    visited=[0]*n
    result = 0
    for node,_ in temp:
        if visited[node]==0:
            explore(adj,node,visited)
            result=result+1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adjr = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adjr[b - 1].append(a - 1)
        
    print(number_of_strongly_connected_components(adj,adjr))
