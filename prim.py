# prim's alg implemented in python
import numpy
import sys
import random
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", action="store_true", dest="stock")

(options, args) = parser.parse_args()

if options.stock:
    print "HEY"

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

print "W = ", W

F = prim(n,W)

print "F = ", F
