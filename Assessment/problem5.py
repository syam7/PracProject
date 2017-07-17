input_ = raw_input("Give the list")


input_ = input_[1:len(input_)-1]
input_ = [int(x) for x in input_.split(',')]

misssing = 0
for i in range(input_[0],input_[len(input_)-1]):
    if i != input_[i-1]:
        missing = i
        break
print "Missing number in the list is ",missing

