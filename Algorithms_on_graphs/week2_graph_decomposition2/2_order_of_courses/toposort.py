#Uses python3

import sys

def explore(adj,v,used):
    global postorder, counter
    used[v]=1
    counter=counter+1
    for w in adj[v]:
        if used[w]==0:
            used=explore(adj,w,used)
    postorder[v]=counter
    counter=counter+1
    return used
    

def dfs(adj, used):
    for i in range(len(adj)):
        if used[i]==0:
            used=explore(adj,i,used)

def toposort(adj):
    global postorder
    n=len(adj)
    used = [0] * n
    dfs(adj,used)
    temp=list(zip(list(range(n)),postorder))
    temp.sort(key=lambda x: x[1],reverse=True)
    order,_=zip(*temp)
    return order
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        
    global postorder,counter
    postorder=[-1]*len(adj)
    counter=0
    
    order=toposort(adj)
    for x in order:
        print(x + 1, end=' ')

