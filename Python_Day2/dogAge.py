age = int(raw_input("Input a dog's age in human years"))

if age<=2:
    new_age = 10.5*age
else :
    new_age = 21+(age-2)*4

print "The dog's age in dog's years is",new_age
