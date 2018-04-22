import numpy as np
import sys
import random
import time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", action="store_true", dest="stock")
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-m", action="store_true", dest="matrix")
parser.add_option("-e", action="store_true", dest="edge_list")
parser.add_option("-d", action="store_true", dest="distance")
parser.add_option("-c", action="store_true", dest="clock")
parser.add_option("-f", action="store_true", dest="file")
parser.add_option("-r", "--random", action="store", type="int", dest="random", help="randomizes edge weights for the adjancency matrix")
parser.add_option("-l", "--limit", action="store", type="int", dest="random_limit", help="upper limit to the randomizer")

(options, args) = parser.parse_args()

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
    vert_list = []

    for i in range(0,n):
        for j in range(0,n):
            row.append(0)
        F_mat.append(row)
        row = []

    print "F_mat = ", F_mat

    print "E = ", E

    # sort E
    E.sort(key=lambda tup: int(tup[2]))
    print "[sort] E = ", E
    
    k = 0
    while ( len(F_list) < (n-1)):
        # print "k = ", k
        e = E[k]
        i = e[0]
        j = e[1]

        # print "e = ", e
        # print "i = ", i
        # print "j = ", j

        if isPromising(i, j, vert_list):
            # yes this can work
            # print "appending : ", e
            F_list.append(e)
            vert_list = appendSet(i, j, vert_list)
            # print "F_list = ", F_list
            # print "vert_list : ", str(vert_list)
            F_mat[i][j] = e[2]

        k = k + 1

        print "========================================"

    print "E = ", E
    print "F_list = ", F_list
    print "F_mat = ", F_mat

    return F_list, F_mat

def get_edge_list(mat):
    n = len(mat[0])
    F_list = []
    inf = sys.maxint
    for i in range(0, n):
        for j in range(i+1, n):
            edge_weight = mat[i][j]
            if edge_weight < (inf - 1):
                F_list.append((i, j, mat[i][j]))
    return F_list

def isPromising(i, j, vert_list):

    # print "len(vert_list) = ", len(vert_list)
    if len(vert_list) == 0:
        return True

    # print "isPromising : vert_list = ", vert_list
    # print "isPromising : len vert_list = ", len(vert_list)
    # print "isPromising : type vert_list = ", type(vert_list)
    # print "isPromising : type vert_list[0] = ", type(vert_list[0])
    # print "isPromising : len vert_list[0] = ", len(vert_list[0])

    a = 0
    b = 0

    for x in range(0, len(vert_list)):
        for y in range(0, len(vert_list[x])-1):
            # print "y+1 : ", y+1
            # print "len(vert_list[x]) : ", len(vert_list[x])
            for z in range (y+1, len(vert_list[x])):
                a = vert_list[x][y]
                b = vert_list[x][z]
                # print "a = ",a
                # print "b = ",b
                if a == i and b == j:
                    return False
    return True

def appendSet(i, j, vert_list):
    theSet = [i, j]
    print "theSet  = ", theSet
    if len(vert_list) == 0:
        vert_list.append(theSet)
        return vert_list

    found = 0

    print "before vert_list = ", vert_list

    for x in range(0, len(vert_list)):
        for y in range(0, (len(vert_list[x])-1)):
            print "outer y = ", y
            for z in range (0, len(vert_list[x])):
                print "y = ",y
                print "z = ",z
                print "i = ",i
                print "j = ",j
                a = vert_list[y][z]
                print "a = ",a
                print ""
                if a == i:
                    # print "set(vert_list[y]) = ", set(vert_list[y])
                    # print "set(vert_list[y]).union(set(theSet)) = ", set(vert_list[y]).union(set(theSet))
                    vert_list[x] = (list(set(vert_list[y]).union(set(theSet))))
                    vert_list = intersect(vert_list)
                    print "1 after vert_list = ", vert_list
                    return vert_list
                if a == j:
                    # print "set(vert_list[y]) = ", set(vert_list[y])
                    # print "set(vert_list[y]).union(set(theSet)) = ", set(vert_list[y]).union(set(theSet))
                    vert_list[x] = (list(set(vert_list[y]).union(set(theSet))))
                    vert_list = intersect(vert_list)

                    print "2 after vert_list = ", vert_list
                    return vert_list

            print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

    vert_list.append(theSet)

    

    print "3 after vert_list = ", vert_list
            
    return vert_list

def intersect(vert_list):
    for x in range (0,len(vert_list)):
        for y in range (x+1, (len(vert_list)) ):
            print "x = ",x
            print "y = ",y
            print "set(vert_list[x]) = ",set(vert_list[x])
            print "set(vert_list[y]) = ",set(vert_list[y])
            if len( set(vert_list[x]) & set(vert_list[y]) ) > 0:
                vert_list[x] = list(set(vert_list[x]).union(set(vert_list[y])))
                vert_list[y] = -1
    
    new_vert_list = []

    for i in range(0,len(vert_list)):
        if vert_list[i] != -1:
            new_vert_list.append(vert_list[i])


    return new_vert_list

# main

if __name__ == "__main__":

    inf = sys.maxint

    if options.random:
        n = options.random
        random_limit = 10
        if options.random_limit:
            random_limit = options.random_limit
        W = []
        row = []
        for i in range(0,n):
            for j in range(0,n):
                row.append(0)
            W.append(row)
            row = []
        for i in range(0,n):
            for j in range(i+1,n):
                W [i][j] = random.randint(1,random_limit)
    else:

        n = 5

        W = [   
                [0,3,inf,11,inf],
                [3,0,12,6,9],
                [inf,12,0,4,4],
                [11,6,4,0,2],
                [inf,9,4,2,0]
            ]
    
    print "W = \n", np.squeeze(np.asarray(W))

    F_list = get_edge_list(W)

    print "edge list = ", F_list
    print "edge list length = ", len(get_edge_list(W))

    m = len(get_edge_list(W))

    K_list, K_mat = kruskal(n, m, F_list)

    # mirror about diagonal
    for i in range(0, n):
        for j in range (0, n):
            K_mat[j][i] = K_mat[i][j]

    print "K_list = ", K_list
    print "K_mat = \n", np.squeeze(np.asarray(K_mat))
    
    # F_list, F_mat = kruskal(n)