# Krusk

```python
def kruskal(n, m, E):
    i = 0
    j = 0
    p = 0
    q = 0
    flag_start = True
    flag_stop = False
    e = (0,0)
    # Sort the me edges in E by weight in nondecreasing order;
    F_list = []
    F_mat = []
    row = []
    start_index_list = []
    stop_index_list = []
    vert_set = set([])
    vert_set_list = []
    candidate = set([])

    # sort E
    E.sort(key=lambda tup: int(tup[2]))
    
    k = 0
    while ( len(F_list) < (n-1)):
        candidate = set( [ E[k][0], E[k][1] ] )

        index_of_set = findLocationOfSet(vert_set_list, candidate)

        if index_of_set != -1:
            num_of_same_verts = len(vert_set_list[index_of_set] & candidate)
        else:
            num_of_same_verts = 0

        # 2-peices of graphs
        if num_of_same_verts == 0:

            # fuse the set
            vert_set_list.append(candidate)

            # append that edge
            F_list.append(E[k])

        # pre-exist graph plus a new vert
        elif num_of_same_verts == 1:

            vert_set_list[index_of_set] = vert_set_list[index_of_set].union(candidate)

            F_list.append(E[k])
        
        k = k + 1

    # return the edge list and matrix
    return F_list

```