n = int(raw_input("0 for C to F and 1 for F to C \n"))
t = int(raw_input("Enter Temperature"))

if n==0:
    con_t =1.8*t+32

else:
    con_t =(t-32)/1.8


print(con_t)
    
    
