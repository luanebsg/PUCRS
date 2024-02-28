import math

# Ideal weight for man or woman

print('Enter 1 for female e 2 for male:')
sex = int(input())
female = 1
male = 2

if sex == female:
  print('Enter the height:')
  height = float(input())
  weight = 62.1 * height - 44.7
  print('The ideal weight for this height is:', weight)
if sex == male:
  print('Enter the height:')
  height = float(input())
  weight = 77.7 * height - 58
  print('The ideal weight for this height is:', weight)
if sex != female and male:
  weight = print('Enter 1 ou 2')

print('End of calculation')

# Duration of a game in a day

print('Consider a day to have 24H')
hourStart = int(input('Enter start hour: '))
minuteStart = int(input('Enter star minute: '))
hourFinish = int(input('Enter finishing hour: '))
minuteFinish = int(input('Enter finishing minute: '))

startTime = hourStart * 60 + minuteStart
finishTime = hourFinish * 60 + minuteFinish

if startTime < finishTime: duration = finishTime - startTime
else: duration = 24 * 60 - startTime + finishTime

print('Hours: ', duration//60)
print('Minutes: ', duration%60)

# Campicua Number

numero = int(input('Informe um valor inteiro de 4 dígitos: '))
if numero < 1111 or numero > 9999: print('Valor inválido: Não tem quatro dígitos')
else:
  milhar = numero//1000
  resto = numero%1000
  centena = resto//100
  resto = resto%100
  dezena = resto//10
  unidade = resto%10
  invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar
  print('Valor ao contrário: ', invertido)
  if numero == invertido: print('Capicua')
  else: print('Não é Capicua')

  # Put in ascending order

value1 = int(input('Enter the first value:'))
value2 = int(input('Enter the second value:'))
value3 = int(input('Enter the third value:'))

higher = value1
if value2 > higher: higher = value2
if value3 > higher: higher = value3

smallest = value1
if value2 < smallest: smallest = value2
if value3 < smallest: smallest = value3

middle = value1 + value2 + value3 - higher - smallest

print('Ascending order: ', smallest, middle, higher)

#Ascending order again

value1 = int(input('Enter the first value:'))
value2 = int(input('Enter the second value:'))
value3 = int(input('Enter the third value:'))

if value2 < value1:
  aux = value1
  value1 = value2
  value2 = aux
if value3 < value1:
  aux = value1
  value1 = value3
  value3 = aux
if value3 < value2:
  aux = value2
  value2 = value3
  value3 = aux

print('Ascending order: ', value1, value2, value3)

# Ascending order again

value1 = int(input('Enter the first value:'))
value2 = int(input('Enter the second value:'))
value3 = int(input('Enter the third value:'))
value4 = int(input('Enter the fourth value:'))


if value2 < value1:
  aux = value1
  value1 = value2
  value2 = aux
if value3 < value1:
  aux = value1
  value1 = value3
  value3 = aux
if value4 < value1:
  aux = value1
  value1 = value4
  value4 = aux
if value3 < value2:
  aux = value2
  value2 = value3
  value3 = aux
if value4 < value2:
  aux = value2
  value2 = value4
  value4 = aux
if value4 < value3:
  aux = value3
  value3 = value4
  value4 = aux

print('Ascending order: ', value1, value2, value3, value4)

# Sales Price

price = float(input('Enter the price cost: '))
if price < 0: print('Invalid price')
else:
  if price < 10: sale = price + (price * 70/100)
  if price >= 10 and price < 30: sale = price + (price * 50/100)
  if price >= 30 and price < 50: sale = price + (price * 40/100)
  if price >= 50: sale = price + (price * 30/100)
print('Sales price = ', sale)

# Printing the day of a week

print('Considering that the week starts on Sunday and ends on Saturday, enter the value 1 to 7 of the desired day: ')
week = int(input())
if week < 1 or week > 7: print('Not a valid week day')
else:
  if week == 1: print('Sunday')
  if week == 2: print('Monday')
  if week == 3: print('Tuesday')
  if week == 4: print('Wednesday')
  if week == 5: print('Thursday')
  if week == 6: print('Friday')
  if week == 7: print('Saturday')
print('End of calculation')


#A weight of a grade

grade1 = float(input('Enter grade 1: '))
grade2 = float(input('Enter grade 2: '))
grade3 = float(input('Enter grade 3: '))

if (grade1 < 0 or grade1 > 10) or (grade2 < 0 or grade2 > 10) or (grade3 < 0 or grade3 > 10): print('Invalid Grade. It must be between [o;10]')
else:
  higher = grade1
  if grade2 > higher: higher = grade2
  if grade3 > higher: higher = grade3
  weight = 0.5 * higher + 0.25 * (grade1 + grade2 + grade3 - higher)
  print('Weight of grade: ', weight)

#Baskara

import math

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
c = int(input('Enter c value: '))

delta = b**2 - 4*a*c
if delta < 0 or a == 0: print('Invalid Number. Delta minor 0 or a == 0')
else:
  x1 = (-b + math.sqrt(delta))/(2 * a)
  x2 = (-b - math.sqrt(delta))/(2 * a)
  print("x1: ", x1)
  print('x2: ', x2)

# Account issues
  
balance = float(input('Enter balance: '))
if balance < 500: print('No limit')
if balance >= 500 and balance < 1000: print('Limit: ', balance * 8/100)
if balance > 1000: print('Limit: ', balance * 15/100)
