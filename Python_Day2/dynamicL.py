row = int(input("Give the number of rows:"))
col = int(input("Give the number of columns:"))

m = [[0 for i in range(col)]for j in range(row)]

for i in range(1,row+1):
    for j in range(1,col+1):
        if i==row:
            m[i-1][j-1] = 1
        elif j==1 and i in range(1,row):
            m[i-1][j-1] = 1


for i in range(1,row+1):
   for j in range(1,col+1):
       if (m[i-1][j-1]==1):
           print ("* "),
       else:
           print ("  "),
   print '\n'
