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
parser.add_option("-f", action="store_true", dest="file")
parser.add_option("-r", "--random", action="store", type="int", dest="random", help="randomizes edge weights for the adjancency matrix")
parser.add_option("-l", "--limit", action="store", type="int", dest="random_limit", help="upper limit to the randomizer")

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

def uniqueify_dble_tup( items ):

    print "================================="
    print ""

    new_items = []

    for i in range(0,len(items)):
        new_items.append(items[i])
    
    for i in range(0, len(new_items) - 1):

        item1 = int(new_items[i][0])
        
        for j in range(i+1, len(new_items)):

            item2 = int(new_items[j][0])

            # print "item1[0] = ", item1
            # print "item2[0] = ", item2
            # print " item1[0] == item2[0] = ",  item1 == item2
            
            if item1 == item2:
                # print "popped = ", new_items[i]
                new_items[i] = (-(i+1),-(i+1))
            # print "new_items = ", str(new_items)

    # print "2 items = ", str(items)

    new_new_items = []

    for i in range (0, len(new_items)):
        if new_items[i][0] > 0:
            new_new_items.append(new_items[i])

    print "leaving! ... new_new_items = ", str(new_new_items)

    print ""
    print "================================="
    return new_new_items

# ==============================================================
# ============================ MAIN ============================
# ==============================================================

if __name__ == "__main__":

    print ""
    print "Start Prim's Algorithm in Python"
    print ""

    inf = sys.maxint

    if options.file:
        file_data = open("data.txt", 'r+')

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
        
        # print "np.squeeze(np.asarray(W)) = \n", np.squeeze(np.asarray(W))

    # Manual entering of adjacency Matrix
    else:

        manual = True
        
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
        for i in range(1,n):
            for j in range(i,n):
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

    if options.verbose or options.stock or manual:
        print "W = \n", np.squeeze(np.asarray(W))

    # Get and print the MST

    if options.clock: 
        clock_start = time.clock()

    # ======================================================
    F_mat, F_list = prim_get_matrix(n,W)
    # ======================================================

    if options.clock: 
        clock_stop = time.clock()
    
    if options.verbose or options.stock or manual:
        print "W = \n", np.squeeze(np.asarray(F_mat))
        print "Edge list = \n", F_list

    # print the combined distane
    d = get_dist_upper_triange(F_mat)
    print "Distance = ",d   


    if options.clock:
        total_clock = clock_stop - clock_start
        print "total_time = ", total_clock, " seconds"

    if options.file and options.clock:

        # sort the file
        file_list = list(file_data)
        file_data.close()
        file_data = open("data.txt", 'w')
        file_n_val = []
        file_time_val = []
        split_line = []
        file_tuples = []

        print "file_list = ",file_list
        for i in range (0, len(file_list)):
            split_line = file_list[i].split(' ')
            file_n_val.append(split_line[0])
            file_time_val.append(split_line[1].split('\n')[0])
            file_tuples.append( (split_line[0], split_line[1].split('\n')[0] ))
        
        file_tuples.append( (str(n),total_clock))

        file_tuples = uniqueify_dble_tup(file_tuples)

        print "[unsort] file_tuples = ", file_tuples

        file_tuples.sort(key=lambda tup: int(tup[0]))

        print "[sort] file_tuples = ", file_tuples

        # write out
        for i in range (0, len(file_tuples)):
            theLine = str(file_tuples[i][0]) + ' ' +  str(file_tuples[i][1]) + '\n' 
            file_data.write(theLine)

        print "file_n_val = ", file_n_val
        print "file_time_val = ", file_time_val
        print "file_tuples = ", file_tuples

        file_data.close()
        # theLine = str(n)+ " " + str(total_clock) + "\n"
        # file_data.write( theLine )
