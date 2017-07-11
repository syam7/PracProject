def isNumThere(s):
    return any(i.isdigit() for i in s)

def isUppCase(s):
    return any(i.isupper() for i in s)

def isLowCase(s):
    return any(i.islower() for i in s)

def specChar(s):
    list = ['$','#','@']
    return any(i in list for i in s)

def lenTest(s):
    return (len(s)>5 and len(s)<17)

import sys
password = sys.argv[1]
s = password

if(isNumThere(s) and isUppCase(s) and isLowCase(s) and specChar(s)and lenTest(s)):
    print("Valid Password")
else:
    print("Not a valid password")
    
