import locale
import datetime
locale.setlocale(locale.LC_TIME, '')  # the ru locale is installed

date = '24 Августа 2022'


temp = date.split()
temp[1] = temp[1][:3]
date = ' '.join(temp)

#
res = datetime.datetime.strptime(date, '%d %b %Y')
print(res)
