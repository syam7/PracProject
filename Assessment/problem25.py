while True:
    try:
        number = int(raw_input("Give a positive number"))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        print "Invalid input"


dict_ = {x:x*x for x in range(1,number+1)}
print dict_
