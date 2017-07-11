row = int(input("Give the number of rows:"))
col = int(input("Give the number of columns:"))

m = [[0 for i in range(col)]for j in range(row)]
mid = (row+1)/2

for i in range(1,row+1):
    for j in range(1,col+1):
        if (i==1 or i==row) and (j in range(2,col)):
            m[i-1][j-1] = 1
        elif (i == mid) and j!=2:
            m[i-1][j-1] = 1
        elif i in range(mid+1,row) and (j==1 or j==col):
            m[i-1][j-1] = 1
        elif i in range(2,mid) and j==1:
            m[i-1][j-1] = 1
        elif i==2 and j== col:
            m[i-1][col-1] = 1


for i in range(1,row+1):
   for j in range(1,col+1):
       if (m[i-1][j-1]==1):
           print ("* "),
       else:
           print ("  "),
   print '\n'
