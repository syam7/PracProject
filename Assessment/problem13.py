while True:
    try:
        number = int(raw_input("Give a positive number"))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        print "Invalid input"

list_ = [number]
while number!=1:
    if number%2==0:
        number = number/2
        list_.append(number)
    else:
        number = 3*number+1
        list_.append(number)

print list_
        
