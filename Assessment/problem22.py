string_ = raw_input("Give the sentence")

len_ = len(string_)
letters = 0
digits = 0

for i in range(0,len_):
    if string_[i].isalpha():
        letters+=1
    elif string_[i].isdigit():
        digits+=1


print "LETTERS",letters
print "DIGITS",digits
