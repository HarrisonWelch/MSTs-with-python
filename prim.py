# prim's alg implemented in python
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
parser.add_option("-r", "--random", action="store", type="int", dest="random", help="randomizes edge weights for the adjancency matrix")

(options, args) = parser.parse_args()

def prim(n, W):
    i = 0
    vnear = 0
    edge = (0,0)
    min = -sys.maxint - 1  
    
    nearest = []
    distance = []
    F = []
    for i in range (0,n):
        # print "i = ",i
        nearest.append(0)
        distance.append(W[0][i])


    # print "=========================================="
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
    # print "=========================================="

    # return the edge list
    return F

def prim_get_matrix(n, W):
    i = 0
    vnear = 0
    edge = (0,0)
    min = -sys.maxint - 1  
    
    nearest = []
    distance = []
    F = []
    for i in range (0,n):
        # print "i = ",i
        nearest.append(0)
        distance.append(W[0][i])

    # print "=========================================="

    new_W = []
    row = []
    for i in range (0,n):
        for j in range(0,n):
            row.append(0)
        new_W.append(row)
        row = []
        

    for x in range (0,n-1):
        min = sys.maxsize
        for i in range(1,n):
            if ( distance[i] >= 0 and distance[i] < min):
                min = distance[i]
                vnear = i
        e = ( vnear, nearest[vnear])
        F.append(e)
        new_W[vnear][nearest[vnear]] = W[vnear][nearest[vnear]]
        distance[vnear] = -1
        for i in range(1,n):
            if ( W[i][vnear] < distance[i] ):
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    # print "=========================================="

    # mirror the matrix
    for i in range(0,n):
        for j in range(0,n):
            if new_W[i][j] == 0:
                new_W[i][j] = new_W[j][i]
            else:
                new_W[j][i] = new_W[i][j] 

    return new_W, F

def get_dist_upper_triange(matrix):
    total = 0
    for i in range(0,n):
        for j in range(i,n):
            total = total + matrix[i][j]
    return total

def get_dist_edge_list(edge_list, matrix):
    total = 0
    for i in range(0,len(edge_list)):
        a = edge_list[i][0]
        b = edge_list[i][1]
        total = total + matrix[a][b]
    return total

# ==============================================================
# ============================ MAIN ============================
# ==============================================================

if __name__ == "__main__":

    print ""
    print "Start Prim's Algorithm in Python"
    print ""

    inf = sys.maxint

    # STOCK data from example Powerpointe
    if options.stock:

        n = 5

        W = [   
                [0,3,inf,11,inf],
                [3,0,12,6,9],
                [inf,12,0,4,4],
                [11,6,4,0,2],
                [inf,9,4,2,0]
            ]

    # Randomizer of edge weights
    elif options.random:
        
        n = options.random
        W = []
        row = []
        for i in range(0,n):
            for j in range(0,n):
                row.append(0)
            W.append(row)
            row = []
        for i in range(0,n):
            for j in range(i+1,n):
                
                W [i][j] = random.randint(1,10)
        

        print "np.squeeze(np.asarray(W)) = \n", np.squeeze(np.asarray(W))


    # Manual entering of adjacency Matrix
    else:
        
        n = 0
        while n < 2:
            n = int(raw_input("Enter 'n' where n >= 2: "))
            print "n = ",n
        W = []
        row = []
        for i in range(1,n):
            for j in range(i,n):
                row.append(0)
            W.append(row)
            row = []
        print "Now start entering edge weights by a number"
        print "Note: Let 'inf' = infinity (non-existent edge)"
        print "Note: The diagonal will be set to all zeroes"
        print ""
        for i in range(0,n):
            for j in range(0,n):
                str_in = input("Enter number for matrix position " + str(i) + ", " + str(j) + ": ")
                if str_in == "inf":
                    W[i][j] = inf
                else:
                    num = int(str_in)
                    W[i][j] = num

        for i in range(0,n):
            W[i][i] = 0

    # mirror

    for i in range(0,n):
        for j in range(i,n):
            W[j][i] = W[i][j]
    
    for i in range(0,n):
        W[i][i] = 0

    if options.verbose:
        print "np.squeeze(np.asarray(W)) = \n", np.squeeze(np.asarray(W))

    # Get and print the MST

    if options.clock: 
        clock_start = time.clock()

    # ======================================================
    F_mat, F_list = prim_get_matrix(n,W)
    # ======================================================

    if options.clock: 
        clock_stop = time.clock()

    print "Resulting edge list is: ", F_list
    print "The number of edges is ", len(F_list)

    
    if options.verbose:
        print "np.squeeze(np.asarray(W)) = \n", np.squeeze(np.asarray(F_mat))

    # print the combined distane
    # d = get_dist_edge_list(F,W)
    d = get_dist_upper_triange(F_mat)
    print "Distance = ",d

    if options.matrix:
        F = prim_get_matrix(n,W)
        print "result edge list for MST: F = ", F_list

    # dist = get_dist_upper_triange(prim_get_matrix(n,W))
    # print "Distance of MST = ", dist

    if options.clock:
        print "total_time = ", (clock_stop - clock_start ), " seconds"
