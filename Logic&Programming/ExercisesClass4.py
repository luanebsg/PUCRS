# Recap of Class3 

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a > b and a > c: print(f'The biggest number is {a}')
if b > a and b > c: print(f'The biggest number is {b}')
if c > a and c > b: print(f'The biggest number is {c}')

# Using nest for the same problem | Class4
# Option 1

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a > b and a > c:
  print(f'The biggest number is {a}')
else:
  if b > a and b > c:
    print(f'The biggest number is {b}')
  else:
    if c > a and c > b:
      print(f'The biggest number is {c}')

# Option 2

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a > b and a > c:
  print(f'The biggest number is {a}')
else:
  if b > a and b > c:
    print(f'The biggest number is {b}')
  else:
      print(f'The biggest number is {c}')

import math
# Calculation of the roots of the second degree equation
# Bhaskara
# Se delta < 0: Não há raíz real  *Personal Note*
# Se delta = 0: Há uma raíz *Personal Note*
# Se delta > 0: Há duas raízes *Personal Note*
# Se houver uma ou duas raízes, fórmula de Bhaskara *Personal Note*

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

delta = (b*b) - 4 * a * c
if delta < 0:
  print('There are no real roots')
else:
  if delta == 0:
    x = -b / (2 * a)
    print(f'The root is {x}')
  else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f'The root is {x1} and {x2}')

# Determine weather conditions from measurements of current temperature and humidity
# Temperature above 30, and humid weather (more than 60%)
# Temperature above 30, and not humid (less than 60%)
# Temperature from 20 to 30
# Temperature 10 to 20 (not including)
# Temperature less than 10
    
    