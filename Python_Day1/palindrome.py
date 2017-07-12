import sys
string = sys.argv[1]
flag = 1

for i in range(len(string)/2):
    if string[i] != string[len(string)-i-1]:
        flag = 0
        break
if flag==1:
    print("Palindrome")
else:
    print("Not a Palindrome")
