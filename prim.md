# prim.md

```python
def prim(n, W):
    i = 0
    vnear = 0
    edge = (0,0)
    min = -sys.maxint - 1  
    nearest = []
    distance = []
    F = []
    for i in range (0,n):
        nearest.append(0)
        distance.append(W[0][i])

    for x in range (0,n-1):
        min = sys.maxsize
        for i in range(1,n):
            if ( distance[i] >= 0 and distance[i] < min):
                min = distance[i]
                vnear = i
        e = ( vnear, nearest[vnear])
        F.append(e)
        distance[vnear] = -1
        for i in range(1,n):
            if ( W[i][vnear] < distance[i] ):
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    return F
```


```python
def get_dist_edge_list(edge_list, matrix):
    total = 0
    for i in range(0,len(edge_list)):
        a = edge_list[i][0]
        b = edge_list[i][1]
        total = total + matrix[a][b]
    return total
```