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
    for i in range (0,n):
        nearest[i] = 1
        distance[i] = i

# ======= MAIN ============================

# if __init__ == "main"

n = 0
while n < 2:
    n = raw_input("Enter 'n' where n>=2: ")

row = []

for i in range(0,n)
    row.append()