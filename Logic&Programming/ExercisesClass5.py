# Range

for cont in range (10, 0, -1):
  print(cont)

# sqrt
  
import math

for num in range (1, 51):
  print(f'{num:6}: {math.sqrt(num):.3f}')

# Acumulação
  
soma = 0
num = int(input("Num: "))

for cont in range (1, num + 1):
  soma = soma + cont
  print(f'{cont}: {soma}')
print(f'Somatório: {soma}')

# Raíz aproximada

num = int(input('Valor Desejado: '))
total = int(input('Qrd. de repetições: '))

aprox = 1
for cont in range (1, total + 1):
  aprox = (aprox + num/aprox) / 2
  print(f'{cont:3}: {aprox:.5f}')

print(f'Raíz aproximada {aprox:.5f}')

# break

for cont in range (20):
  if cont > 10:
    break
  print(cont)
print('Continuação')

# continue

for cont in range (20):
  if cont % 2 == 1:
    continue
  print(cont)
print('Continuação')