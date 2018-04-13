# prim's alg implemented in python
import numpy
import sys
import random
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", action="store_true", dest="stock")
parser.add_option("-v", action="store_true", dest="verbose")
parser.add_option("-m", action="store_true", dest="matrix")
parser.add_option("-e", action="store_true", dest="edge_list")
parser.add_option("-d", action="store_true", dest="distance")

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

    # print "nearest = ", nearest
    # print "distance = ", distance
    # print "min = ", min

    # print "=========================================="
    # repeat n-1 times
    for x in range (0,n-1):
        min = sys.maxsize
        for i in range(1,n):
            # print "distance[i] = ", distance[i]
            # print "min = ", min
            # print "i = ",i
            # if( 0 <= distance < min)
            if ( distance[i] >= 0 and distance[i] < min):
                # print "         setting min = ",distance[i]
                min = distance[i]
                vnear = i
        e = ( vnear, nearest[vnear])
        # print "e = ",e
        F.append(e)
        distance[vnear] = -1
        for i in range(1,n):
            if ( W[i][vnear] < distance[i] ):
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    # print "=========================================="
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

    # print "nearest = ", nearest
    # print "distance = ", distance
    # print "min = ", min

    # print "=========================================="
    # repeat n-1 times

    new_W = []
    row = []
    for i in range (0,n):
        for j in range(0,n):
            row.append(0)
        new_W.append(row)
        row = []
        

    print "new_W = ", new_W

    for x in range (0,n-1):
        min = sys.maxsize
        for i in range(1,n):
            # print "distance[i] = ", distance[i]
            # print "min = ", min
            # print "i = ",i
            # if( 0 <= distance < min)
            if ( distance[i] >= 0 and distance[i] < min):
                # print "         setting min = ",distance[i]
                min = distance[i]
                vnear = i
        e = ( vnear, nearest[vnear])
        # print "e = ",e
        F.append(e)
        print "new_W = ", new_W
        print "vnear = ", vnear
        new_W[vnear][nearest[vnear]] = W[vnear][nearest[vnear]]
        print "nearest[vnear] = ", nearest[vnear]
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

    return new_W

def get_dist_upper_triange(matrix):
    total = 0
    for i in range(0,n):
        for j in range(i,n):
            total = total + matrix[i][j]
    return total


# ======= MAIN ============================

# if __init__ == "main"

# n = 0
# while n < 2:
#     n = int(raw_input("Enter 'n' where n>=2: "))

# row = []
# W = []

# for i in range(0,n):
#     for j in range(0,n):
#         row.append(random.randint(0,10))
#         # print "row = ", row
#     W.append(row)
#     row = []



inf = sys.maxint

if options.stock:

    W = [   
            [0,3,inf,11,inf],
            [3,0,12,6,9],
            [inf,12,0,4,4],
            [11,6,4,0,2],
            [inf,9,4,2,0]
        ]

    n = 5

else:
    n = 0
    while n < 2:
        n = int(raw_input("Enter 'n' where n >= 2: "))


for i in range(0,n):
    for j in range(i,n):
        W[i][j] = W[j][i]

for i in range(0,n):
    W[i][i] = 1

if options.verbose:
    print "W = ", W

print "Resulting edge list is: "
F = prim(n,W)
print F

if options.matrix:
    F = prim_get_matrix(n,W)
    print "result edge list for MST: F = ", F

if options.distance:
    dist = get_dist_upper_triange(prim_get_matrix(n,W))
    print "dist = ", dist
