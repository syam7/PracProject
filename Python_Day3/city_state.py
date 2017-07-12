dict = {'kolkata':'West Bengal','hyderabad':'Telangana','mumbai':'Maharashtra','bangalore':'Karnataka'}
#print dict[raw_input("Give the City")]
new_dict = {k:v for k,v in zip(dict.values(),dict.keys())}
print new_dict[raw_input("Give the State")]
