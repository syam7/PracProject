import collections


string_ = raw_input("Give the input")
string_ = string_.split()

counter = collections.Counter(string_)
x = sorted(counter)


for temp in x:
    print temp,counter[temp]
