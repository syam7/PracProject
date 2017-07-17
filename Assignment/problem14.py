y = int(raw_input("Input a year: "))
m = int(raw_input("Input a month [1-12]: "))
d = int(raw_input("Input a day [1-31]: "))

if (y % 400 == 0):
    leap = True
elif (y % 100 == 0):
    leap = False
elif (y % 4 == 0):
    leap = True
else:
    leap = False

m_list = [1, 3, 5, 7, 8, 10, 12]
if m in m_list:
    mlength = 31
elif m == 2:
    if leap:
        mlength = 29
    else:
        mlength = 28
else:
    mlength = 30


if d < mlength:
    d += 1
else:
    d = 1
    if m == 12:
        m = 1
        y += 1
    else:
        m += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (y, m, d))
