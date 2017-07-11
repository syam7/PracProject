from __future__ import print_function
import sys
n = int(sys.argv[1])
x,y = 0,1
while(y<=n):
    print(y,end=" ")
    x,y = y,x+y
