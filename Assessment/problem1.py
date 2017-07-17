while True:
    try:
        number = int(raw_input("Give a number"))
        break
    except ValueError:
        print "This is not a valid number"
