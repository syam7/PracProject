import sys

print "Addition:0","Subtraction:1","Multiplication:2","Division:3","Exit:4"

oper = raw_input("Give the operation number")
list_oper = ['0','1','2','3','4']
if oper not in list_oper:
    print("Give the number in the above specified operations")
    sys.exit()

while (oper in list_oper):
    if(oper=='4'):
        break

    a,b = map(float,raw_input("Give the two numbers: ").split())

    if(oper=='0'):
        print "Addition of two numbers is",(a+b)
    elif(oper=='1'):
        print "Subtraction of two numbers is",(a-b)
    elif(oper=='2'):
        print "Multiplication of two numbers is",(a*b)
    elif(oper=='3'):
        print "Division of two numbers is",(a/b)
    

    oper = raw_input("Give the operation number")

    

