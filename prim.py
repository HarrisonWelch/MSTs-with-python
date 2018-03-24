# prim's alg implemented in python
import numpy
import sys
import random

def prim(n, W):
    i = 0
    vnear = 0
    edge = (0,0)
    min = -sys.maxint - 1  
    
    nearest = []
    distance = []
    F = []
    for i in range (0,n):
        print "i = ",i
        nearest.append(1)
        distance.append(W[0][i])

    

    for x in range (0,n-1):

        min = sys.maxsize
        for i in range(1,n):
            if ( 0 <= distance[i] and distance[i] < min):
                min = distance[i]
                vnear = i
        e = ( vnear, nearest[vnear])
        F.append(e)
        distance[vnear] = -1
        for i in range(1,n):
            if ( W[i][vnear] < distance[i] ):
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    return W


# ======= MAIN ============================

# if __init__ == "main"

n = 0
while n < 2:
    n = int(raw_input("Enter 'n' where n>=2: "))

row = []
W = []

for i in range(0,n):
    for j in range(0,n):
        row.append(random.randint(1,10))
        print "row = ", row
    W.append(row)
    
    row = []

print "W = ", W

W = prim(n,W)

print "W = ", W
