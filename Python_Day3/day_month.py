
days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
days_num = (1,2,3,4,5,6,7)
months = ('january','february','march','april','may','june','july','august','september','october','november','december')
months_num = (1,2,3,4,5,6,7,8,9,10,11,12)

days_dict = {k:v for k,v in zip(days,days_num)}
months_dict = {k:v for k,v in zip(months,months_num)}


inp = raw_input("Give a day or month")
inp = inp.lower()

if inp in days:
    print days_dict[inp]
else:
    print months_dict[inp]
