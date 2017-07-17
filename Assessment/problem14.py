while True:
    try:
        number = int(raw_input("Give a positive number"))
        if number <= 0:
            raise ValueError
        break
    except ValueError:
        print "Invalid input"


flag = 0

while flag ==0 and number!=1:
    if number%2 == 0:
        number = number/2
    else:
        flag = 1


if flag == 0:
    print "Given Number is a power of 2"
else:
    print "Given Number is not a power of 2"
