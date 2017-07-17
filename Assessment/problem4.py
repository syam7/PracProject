
number = int(input("Give the number"))
sum_digits = 0

while number:
    temp = number%10
    number = number/10
    sum_digits+=temp

print "Sum of digits of number is ",sum_digits
