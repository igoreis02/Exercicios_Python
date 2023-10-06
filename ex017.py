import math
cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))
#hip = math.sqrt(cat_op ** 2 + cat_ad ** 2)
hip = math.hypot(cat_op, cat_ad)
print('A hipotenusa é : {:.2f}'.format(hip))
