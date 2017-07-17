filename = "practise.txt"

for line in reversed(open(filename).readlines()):
    print line.rstrip()
