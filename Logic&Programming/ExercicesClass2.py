# Exercício 1

import math
print('Informe o Valor do raio: ')
raio = float(input())
volume = 4/3 * math.pi * raio ** 3
print('Volume:', volume)

# Exercício 2

import math
print('Informe o valor do raio:')
raio = float(input())
a = 4 * math.pi * raio ** 2
print('Área:', a)

#Como eu fiz, ex3

import math
print('Informe o valor de n:')
n = float(input())
p0 = n**2
p1 = n**3
p2 = n**4
print('Resultado de n**2:', p0)
print('Resultado de n**3:', p1)
print('Resultado de n**4:', p2)

# Como a prof fez

print('Informe um valor:')
n = float(input())
print('Quadrado do valor', n**2)
print('Cubo do valor', n**3)
print('Valor na quarta', n**4)

# Fahrenheit

print('Informe o valor de Fahrenheit:')
f = float(input())
c = 5/9*(f-32)
print('Convertido em Celcius:', c)

# Conversão de segundos decomposto em hora, minuto e segundo.

print('Insira os segundos:')
seg = int(input())
h = seg//3600
m = (seg%3600)//60
s = seg%60
print('Decomposição em hora:', h)
print('Decomposição em minuto:', m)
print('Decomposição em segundo:', s)

# Leitura da ordem inversa do input

print('Informe um valor inteiro de 4 dígitos:')
value = int(input())
m = value//1000
resto = value % 1000
c = resto // 100
resto = resto % 100
d = resto // 10
u = resto % 10
print('Valor ao contrário:', u*1000 + d*100 + c*10 + m )