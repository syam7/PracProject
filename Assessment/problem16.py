filename = "practise.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

print len(lines)
