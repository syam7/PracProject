from __future__ import print_function
def printtop():
    print("  ",end="")
    for i in range(3):
        print("* ",end="")
    print("")
    

def printmid():
    for i in range(5):
        print("* ",end="")
    print("")

def printdown():
    print("* ", end="")
    for i in range(3):
        print("  ",end="")
    print("* ")

if __name__=="__main__":

    printtop()
    printdown()
    printdown()
    printmid()
    printdown()
    printdown()
    printdown()
