import math

print('Løser likningen ax² + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

diskriminant = b**2 - 4*a*c

if diskriminant < 0:
    svar = []
elif diskriminant == 0:
    svar = [-b / 2*a]
else:
    x1 = (-b + math.sqrt(diskriminant)) / 2*a
    x2 = (-b - math.sqrt(diskriminant)) / 2*a
    svar = [x1, x2]
print('svar =', svar)
