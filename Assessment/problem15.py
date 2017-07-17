tup_list = eval(raw_input("Enter a list of tuples:"))

x = sorted(tup_list,key=lambda x:x[-1])

print x


