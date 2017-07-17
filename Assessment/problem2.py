string_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

temp=0
for i in range(1,6):
    for j in range(temp,temp+i):
       
        print string_[j],
        temp = j+1
     
    print ""
