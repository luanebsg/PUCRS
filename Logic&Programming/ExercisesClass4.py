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

# The game Rock, Paper, Scissors
# • Rules (victory conditions)
# 1. Scissors cut the paper
# 2. Paper wraps the stone
# 3. Rock breaks scissors
# 4. If they both use the same move it is a tie

import random

player = input('Choose: [R]ock, [P]aper or [S]cissors?')
pc = random.choice(["R", "P", "S"])
print(f"Computers Choice: {pc}")

if player == pc:
  print(f'Draw!')
elif player == "R":
  if pc == "S":
    print('R breaks S! You Won!')
  else:
    print('P covers R! You Lost!')
elif player == "P":
  if pc == "R":
    print('P covers R! You Won!')
  else:
    print('S cut P! You Lose!')
elif pc == "P":
  print('S cut P! You Won!')
else:
  print('R breaks S! You Lose!')

  # A year is a leap year if
# • …is divisible by 4
# • …but not by 100, unless it is divisible by 400
# • Write a program that takes as input one year and determines whether it is a leap year or not.
# • How to structure the logic?

year = int(input('Year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("It's a Leap Year")
else:
  print("It's not a Leap Year")

# Based on the months example, write a program that determine the number of days in a month and year informed.
# • Remember that some months have 30, others have 31 and one of them has 28 (or 29, if the year is a leap year).

month = int(input('Month: '))
year = int(input('Year: '))

if month == 2:
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days = 29
  else:
    days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
  days = 30
else:
  days = 31
print(f'Total of days: {days}')

# Net salary calculation
# Inputs: gross salary and total dependents
# Outputs:
# INSS discount
# IRRF discount (tax withheld at source)
# Net salary
# The acronyms are based on Brazilian taxes

gross = float(input("Gross Income: "))
dep = int(input("Number of people depending on you: "))

# INSS calculation
if gross < 1212.01:
    alinss = 0.075
    parcinss = 0
elif gross <= 2427.35:
    alinss = 0.09
    parcinss = 18.18
elif gross <= 3641.03:
    alinss = 0.12
    parcinss = 91
else:
    alinss = 0.14
    parcinss = 163.82

inss = gross * alinss - parcinss

if inss > 828.39:
    inss = 828.39  # limited
print(f"INSS: {inss}")

# IRRF calculation
baseIncome = gross - inss - (189.59 * dep)
print("Base Income Calculation:", baseIncome)

if baseIncome <= 1903.98:
    aliqirrf = 0
    parcirrf = 0
elif baseIncome <= 2826.65:
    aliqirrf = 0.075
    parcirrf = 142.8
elif baseIncome <= 3751.05:
    aliqirrf = 0.15
    parcirrf = 354.8
elif baseIncome <= 4664.68:
    aliqirrf = 0.225
    parcirrf = 636.13
else:
    aliqirrf = 0.275
    parcirrf = 869.36 

irrf = baseIncome * aliqirrf - parcirrf

print("IRRF:", irrf)

net = gross - inss - irrf
print("Net Salary:", net)
