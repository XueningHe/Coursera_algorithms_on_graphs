#Uses python3
import sys
import math
import numpy as np

def union(set_dict,u,v):
    set_num_to_merge=set_dict[v]
    for key in set_dict.keys():
        if set_dict[key]==set_num_to_merge:
            set_dict[key]=set_dict[u]
    return set_dict
    

def kruskal(n,edges):
    set_dict={}
    X=[]
    for i in range(n):
        set_dict[i]=i
    edges.sort(key=lambda x: x[2])
    for u,v,w in edges:
        if not set_dict[u]==set_dict[v]:
            X.append((u,v,w))
            set_dict=union(set_dict,u,v)
    return X


def minimum_distance(x, y):
    n=len(x)
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            dist=np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            edges.append((i,j,dist))
    X=kruskal(n,edges)
    dist=[x[2] for x in X]
    return sum(dist)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
