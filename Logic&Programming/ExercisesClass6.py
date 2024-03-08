# FOR e WHILE

num = 1

for num in range (1,11):
  print(num)
  break

while num <= 10:
  print(num)
  num = num + 1


#Fatorial, DECREMENTANDO

#As variáveis para soma iniciam com 0, mas as variáveis para multiplicação iniciam com 1.

valor = int(input('Informe um valor natural: '))
fat = 1
aux = 2

while aux <= valor:
  fat = fat * aux
  aux = aux + 1
print(f'Fatorial: {fat}')

#Divisores de um número

valor = int(input('Informe um valor natural: '))
d = 1
while d <= valor:
  if valor % d == 0: print(d, 'divide', valor)
  d = d + 1

# Exercício – Implemente um programa que leia um valor inteiro e
# que verifica se o valor lido e’ primo. Números primos possuem
# apenas 2 divisores.
# Exemplos de números primos: 2, 3, 5, 7, 11, 13, ...

num = int(input('Digite um valor natural: '))
cont = 0
d = 1

while d <= num:
  if num % d == 0:
    cont = cont + 1
  d = d + 1

if cont == 2:
  print(f'{num} É primo.')
else:
  print(f'{num} Não é primo')

# 1. Implemente um programa que calcula a soma do n primeiros termos da serie a seguir:
# 1 + ½ + 1/3 + ¼ + 1/5 + ....

nTermos = int(input('Informe a quantidade de termos: '))
if nTermos <= 0: print('Número Inválido')
else:
  soma = 0
  cont = 1
  while cont <= nTermos:
    soma = soma + 1/cont
    cont = cont + 1
  print(f'Soma: {soma}')

# 2. Implemente um programa que calcula a soma do n primeiros termos da serie a seguir:
# 2 + 4/3 + 6/5 + 8/7 + 10/9 + ....

nTermos = int(input('Informe a quantidade de termos: '))
if nTermos <= 0: print('Número Inválido')
else:
  soma = 0
  cont = 1
  numerador = 2
  denominador = 1
  while cont <= nTermos:
    soma = soma + numerador/denominador
    cont = cont + 1
    numerador = numerador + 2
    denominador = denominador + 2
  print(f'Soma: {soma}')

# 3. Implemente um programa que leia dois valores a e b. O
# programa deve escrever e somar os valores impares
# existentes entre a e b.
# Exemplo: a = 10 e b = 16
# 11, 13, 15
# Soma = 39

a = int(input('Informe o valor inicial do intervalo: '))
if a < 0: print('O valor deve ser natural.')
else:
  b = int(input('Informe o valor final do intervalo: '))
  if b < 0: print('O valor deve ser natural.')
  else:
    if a > b:
      aux = a
      a = b
      b = aux
    if a % 2 == 0: a = a + 1
    soma = 0
    print('Valores ímpares do  intervalo: ')
    while a <= b:
      print(a)
      soma = soma + a
      a = a + 2
    print(f'Soma dos ímpares do intervalo = {soma}')

# 4. Implemente um programa que leia um valor e verifique se
# e’ perfeito. Para ser perfeito, ele deve corresponde ‘a soma
# dos seus divisores próprios.
# Exemplo: 6, pois 1 +2 + 3 e’ 6.

num = int(input('Informe um valor inteiro e positivo: '))
while num <= 0:
  print('Valor deve ser positivo')
  num = int(input('Informe um valor inteiro e positivo: '))

soma = 0
d = 1
while d <= num // 2:  # Usar divisão inteira para garantir que d seja um inteiro
    if num % d == 0:
        soma += d
    d += 1

if soma == num:
    print('Número é perfeito')
else:  # Corrigido a indentação do else
    print('Número não é perfeito')

# 1. Chico tem 1,50 metro e cresce 2 centímetros por ano,
# enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano.
# Construa um programa que calcule e exiba quantos anos
# serão necessários para que Zé seja maior que Chico.

altChico = 150
altZe = 110
anos = 0
mais20 = 0

while altZe <= altChico:
  altChico = altChico + 2
  altZe = altZe + 3
  anos = anos + 1
print(f'Anos: {anos}')

# 2. Implemente um programa que leia a idade, altura e
# gênero de 10 estudantes. O programa deve calcular e
# escrever:
# a) Media de idade dos estudantes
# b) Media de altura das meninas
# c) Percentual de estudantes com mais de 20 anos.
# d) Altura do estudante mais velho
# Valide/Critique os dados de entrada

#Solução Determinada

cont = 0
somaIdade = 0
somaAltura = 0
meninas = 0
mais20 = 0
maiorIdade = 0
maiorAltura = 0

while cont < 3:
  print(f'Cont: {cont}')
  idade = int(input('Informe sua idade: '))
  while idade <= 0 or idade >= 120:
    print('Idade Inválida.')
    idade = int(input('Informe novamente sua idade: '))

  altura = float(input('Informe sua altura: '))
  while altura <= 0 or altura >= 2.5:
    print('Altura Inválida.')
    altura = float(input('Informe novamente a sua altura: '))

  genero = int(input('Informe seu gênero usando 1 para Feminino e 2 par Masculino: '))
  while genero != 1 and genero != 2:
    print('Gênero inválido.')
    genero = int(input('Informe novamente seu gênero: '))

  #(a)
  somaIdade = somaIdade + idade
  cont = cont + 1
  #(b)
  if genero == 1:
    somaAltura = somaAltura + altura
    meninas = meninas + 1
  #(c)
  if idade > 20:
    mais20 = mais20 + 1
  #(d)
  if idade > maiorIdade:
    maiorIdade = idade
    maiorAltura = altura

print('===============================================')
print(f'Média de idade dos estudantes: {somaIdade/cont}')
if meninas == 0 : print('Não foram informados dados de meninas.')
else: print(f'Média altura menina: {somaAltura/meninas}')
print(f'Percentual de alunos com mais de 20 anos: {mais20 * 100/cont}')
print(f'Altura do mais velho: {maiorAltura}, idade do mais velho: {maiorIdade}')

#Solução Indeterminada

cont = 0
somaIdade = 0
somaAltura = 0
meninas = 0
mais20 = 0
maiorIdade = 0
maiorAltura = 0

while True:
  print(f'Cont: {cont}')
  print('Para encerrar a repetição, informe uma idade negativa.')
  idade = int(input('Informe sua idade: '))
  if idade < 0:
    print('Fim de programa')
    break
  while idade <= 0 or idade >= 120:
    print('Idade Inválida.')
    idade = int(input('Informe novamente sua idade: '))

  altura = float(input('Informe sua altura: '))
  while altura <= 0 or altura >= 2.5:
    print('Altura Inválida.')
    altura = float(input('Informe novamente a sua altura: '))

  genero = int(input('Informe seu gênero usando 1 para Feminino e 2 par Masculino: '))
  while genero != 1 and genero != 2:
    print('Gênero inválido.')
    genero = int(input('Informe novamente seu gênero: '))

  #(a)
  somaIdade = somaIdade + idade
  cont = cont + 1
  #(b)
  if genero == 1:
    somaAltura = somaAltura + altura
    meninas = meninas + 1
  #(c)
  if idade > 20:
    mais20 = mais20 + 1
  #(d)
  if idade > maiorIdade:
    maiorIdade = idade
    maiorAltura = altura

print('===============================================')
if cont == 0:
  print('Dados não informados.')
else:
  print(f'Média de idade dos estudantes: {somaIdade/cont}')
  if meninas == 0 : print('Não foram informados dados de meninas.')
  else: print(f'Média altura menina: {somaAltura/meninas}')
  print(f'Percentual de alunos com mais de 20 anos: {mais20 * 100/cont}')
  print(f'Altura do mais velho: {maiorAltura}, idade do mais velho: {maiorIdade}')

# Tabuada

for numero in range (1,11):
  for valor in range (1,11):
    print(numero, 'x', valor, '=', numero*valor)
  print()

numero = 1
while numero <= 10:
  valor = 1
  while valor <= 10:
    print(numero, 'x', '=', numero*valor)
    valor = valor + 1
  print()
  numero = numero + 1

# Implemente um programa que escreve os divisores dos 100
# primeiros valores inteiros.

for num in range (1,101):
  print('>> Número: ',num)
  d = 1
  while d <= num:
    if num % d == 0: print(d, 'divide', num)
    d = d + 1

# Implemente um programa que escreve os n primeiros
# números primos.

quant = int(input('Informe a quantidade de números primos: '))
while quant <= 0:
  print('Valor inválido. A quantidade deve ser positiva.')
  quant = int(input('Informe a quantidade de números primos: '))


num = 2
primos = 0

while primos < quant:
  contaDivisores = 0
  d = 1
  while d <= num:
    if num % d == 0: contaDivisores = contaDivisores + 1
    d = d + 1
  if contaDivisores == 2:
    print(num)
    primos = primos + 1
  num = num +1


num = int(input('Informe um valor par maior que 4: '))

parte1 = num // 2
parte2 = parte1

while parte2 >= 2:  # Ajustado para garantir que parte2 não seja menor que 2
    contParte1 = 0
    d = 2  # Iniciar de 2, pois 1 não é considerado na contagem de divisores para primos
    while d < parte1:  # Ajuste para contar corretamente os divisores de parte1
        if parte1 % d == 0: 
            contParte1 += 1
        d += 1

    if contParte1 == 0:  # Isso significa que parte1 é primo
        d = 2  # Resetar d para verificar parte2
        contParte2 = 0
        while d < parte2:  # Ajuste para contar corretamente os divisores de parte2
            if parte2 % d == 0: 
                contParte2 += 1
            d += 1
        if contParte2 == 0:  # Isso significa que parte2 também é primo
            print('Primo1:', parte1, 'Primo2:', parte2)
            break
    parte1 += 1
    parte2 -= 1

# Construa um programa que escreve o fatorial dos 100 primeiros inteiro.

num = 0

while num <= 99:
  fat = 1
  while aux <= num:
    fat = fat * aux
    aux = aux + 1
  print(f'O Fatorial de {num} é {fat}.')
  num = num + 1

# – Escreva um programa que leia uma quantidade
# desconhecida de números. A seguir, o programa deve contar e
# escrever a quantidade de valores pertencentes aos seguintes
# intervalos: [0;25], [26;50], [51;75] e [76;100]. A entrada de
# dados deve terminar quando for lido um número negativo. Ao
# final o programa deve exibir ainda a quantidade de valores lidos.

total = 0
cont0_25 = 0
cont26_50 = 0
cont51_75 = 0
cont76_100 = 0

while True:
  print('Informe um valor negativo para encerrar a repetição.')
  valor = int(input('Informe um valor inteiro: '))
  if valor < 0:
    print('Fim do Programa.')
    break
  if valor <= 25:
    cont0_25 = cont0_25 + 1
  else:
    if valor < 50:
      cont26_50 = cont26_50 + 1
    else:
      if valor <= 75:
        cont51_75 = cont51_75 + 1
      else:
        if valor <= 100:
          cont76_100 = cont76_100 + 1
  total = total + 1

print('==========================================================')
print(f'Quantidade de valores digitados: {total}')
print(f'Quantidades de valores no intervalo [0,25]: {cont0_25}')
print(f'Quantidades de valores no intervalo [26,50]: {cont26_50}')
print(f'Quantidades de valores no intervalo [51,75]: {cont51_75}')
print(f'Quantidades de valores no intervalo [76,100]: {cont76_100}')

# Foi feita uma pesquisa entre os habitantes de uma
# região. Foram coletados os dados de idade, sexo (1-masculino/2-
# feminino) e salário. Faça um programa que leia os dados
# necessário e informe:
# (a)a média de salário do grupo;
# (b) maior e menor idade do grupo;
# (c) quantidade de mulheres com salário até R$3500,00.
# Encerre a entrada de dados quando for digitada uma idade
# negativa


somaSalario = 0
pessoas = 0
maior = 0
menor = 120
mulheres = 0

while True:
  print('Informe uma idade negativa para encerrar a entrada de dados.')
  idade = int(input('Informe uma idade: '))
  if idade < 0:
    print('Fim do programa.')
    break

  while idade <= 0 or idade >= 120:
    print('Idade inválida. Deve estar no intervalo de (0,120).')
    idade = int(input('> Informe uma idade válida: '))
  
  genero = int(input('Informe o gênero usando 1 para Feminino e 2 para Masculino: '))
  while genero != 1 and genero != 2:
    print('Gênero Inválido.')
    genero = int(input('Informe novamente o gênero, usando 1 para Feminino e 2 para Masculino: '))

  salario = float(input('Informe o salário: '))
  while salario < 0:
    print('Salário Inválido.')
    salario = float(input('Informe o salário: '))

  somaSalario = somaSalario + salario
  pessoas = pessoas + 1
  if idade > maior:
    maior = idade
  if idade < menor:
    menor = idade
  if genero == 1 and salario <= 3500:
    mulheres = mulheres + 1

print('================================================================')
if pessoas == 0:
  print('Dados não informados.')
else:
  print(f'Média de Salário: {somaSalario/pessoas}')
  print(f'Maior idade: {maior}')
  print(f'Menor idade: {menor}')
  print(f'Quantidade de mulheres que ganham até R$3500: {mulheres}')

