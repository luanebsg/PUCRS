# Crie uma lista com 30 valores inteiros. Gere a lista com valores
# aleatorios entre 1 e 500. A seguir, implemente um programa
# que varre a lista, calcula e exibe:
# a) O maior valor da lista
# b) A quantidade de pares

import random

lista = [] #lista vazia

for i in range(1,31):
  lista.append(random.randint(1,500))
print(lista)

maior = lista[0]
pares = 0

for num in lista:
  if num > maior: maior = num
  if num % 2 == 0: pares = pares + 1

print(f'Maior: {maior}')
print(f'Quantidade de pares: {pares}')

# Defina uma lista com as notas de 15 alunos. O programa deve
# contar e escrever quantos alunos estão
# • acima da média.
# • na média.
# • abaixo da média.
# Escrever também a maior e menor nota.

lista = [] #lista vazia

for i in range (1,16):
  lista.append(random.randint(1,100)/10)
print(f'Notas: {lista}')

media = sum(lista)/len(lista)
print(f'Média: {media}')

acima = 0
abaixo = 0

for nota in lista:
  if nota > media: acima = acima + 1
  if nota < media: media = media + 1

print(f'Quantidade de noas acima da média: {acima}')
print(f'Quantidade de notas abaixo da média: {abaixo}')
print(f'Quantidade de notas iguais a média: {lista.count(media)}')
print(f'Maior nota: {max(lista)}')
print(f'Menor nota: {min(lista)}')

# Construa um programa que gera uma lista com as
# avaliações de 25 pessoas. Cada pessoa avaliou a gestão do
# prefeito de uma cidade com notas de 5 a 1, onde 5 corresponde
# a Excelente, 4 a Bom, 3 a Regular, 2 a Ruim e 1 a Péssimo. Seu
# programa deve calcular e escrever:
# • A quantidade de votos em cada conceito.

import random

lista = [] #lista vazia

for i in range (1,26):
  lista.append(random.randint(1,6))
print(f'Notas: {lista}')

conceito = []
quantidade = []

conceito.append('Excelente')
quantidade.append(lista.count(5))

conceito.append('Bom')
quantidade.append(lista.count(4))

conceito.append('Regular')
quantidade.append(lista.count(3))

conceito.append('Ruim')
quantidade.append(lista.count(2))

conceito.append('Péssimo')
quantidade.append(lista.count(1))

maiorQuantidade = quantidade [0]
maiorConceito = conceito [0]

for i in range (0,5):
  print(conceito[i], ' - ', quantidade[i])
  if quantidade[i] > maiorQuantidade:
    maiorQuantidade = quantidade[i]
    maiorConceito = conceito[i]

print(f'Conceito mais votado: {maiorConceito}')
print(f'Recebeu {maiorQuantidade} votos.')

# Defina uma lista com a idade de 20 pessoas. Seu
# programa deve calcular e escrever: média de idade, maior e
# menor idade.

import random

pessoas = []

for i in range (1,21):
  pessoas.append(random.randint(1,121))
print(f'Idade das pessoas: {pessoas}')

media = sum(pessoas)/len(pessoas)
print(f'Média de idade: {media}')
print(f'Maior idade: {max(pessoas)}')
print(f'Menor idade: {min(pessoas)}')


# Elabore um programa que gera uma lista com 30
# valores inteiros, cria e escreve uma outra lista com os 10 maiores.

import random

lista1 = []

for i in range (1,31):
  lista1.append(random.randint(1,100))
print(f'Lista 1 com números inteiros: {lista1}')

lista1.sort()
print(lista1)

lista1.reverse()
print(lista1)

index = 0
maiores = []

while (index < 10):
  maiores.append(lista1[index])
  index = index + 1
print(f'Dez maiores: {maiores}')

# Uma empresa de estatística analisou os 5 melhores jogadores de
# uma liga profissional de basquete e registrou os pontos,
# assistências e rebotes de cada um. Para isso, crie uma lista de
# tuplas, onde cada tupla é da forma (nome do jogador, pontos,
# assistência, rebotes). Ao final, o programa deve percorrer a lista
# e informar a tupla do jogador que tem as melhores estatísticas
# ((pontos+assistências+rebotes)/3).

jogadores = []
cont = 1

while cont <= 5:
  print(f'Cont: {cont}')
  nome = input('Informe o nome do jogador: ')
  pontos = int(input('Informe os pontos feitos: '))
  assistencias = int(input('Informe as assistências feitas: '))
  rebotes = int(input('Informe o número de rebotes: '))
  jogadores.append((nome, pontos, assistencias, rebotes))
  cont = cont + 1
print(jogadores)

estatisticas = []

for dados in jogadores:
  soma = 0
  for i in range (1,4):
    soma = soma + dados[i]
  media = soma / 3
  estatisticas.append((dados[0], media))
print(estatisticas)

# Correção do loop para encontrar o melhor jogador
melhor = estatisticas[0]  # Assumindo que o primeiro jogador é o melhor inicialmente

for item in estatisticas:
  if item[1] > melhor[1]:  # Compara a média do jogador atual com a do melhor atual
    melhor = item

print(f'Melhor jogador: {melhor[0]}, Média: {melhor[1]}')


# Foram vendidas 50 peças de roupa. De cada peça
# foram coletados os seguintes dados: tamanho (P,M ou G) e cor
# (branco, preto ou azul). O programa deve ler os dados das peças
# de roupas e organizá-los em uma lista de tuplas, onde cada tupla
# é da forma (tamanho, cor). O programa deve ainda calcular e
# escrever: o tamanho que mais vendeu, a quantidade de peças de
# tamanho M que foram vendidas e a cor preferida pelos clientes.

roupas = []
for i in range (1,6):
  print(f'Cont: {i}')
  tamanho = input('Informe os tamanhos usando P,M,G: ')
  while (tamanho != 'P' and tamanho != 'p' and tamanho != 'M' and tamanho != 'm' and tamanho != 'G' and tamanho != 'g'):
    tamanho = input('Informe os tamanhos usando P,M,G: ')
  op = int(input('Informe 1 para Branco, 2 para Preto e 3 para Azul: '))
  while (op < 1 or op > 3):
    op = int(input('Informe 1 para Branco, 2 para Preto e 3 para Azul: '))
  if op == 1: tupla = (tamanho, 'Branco')
  else:
    if op == 2: tupla = (tamanho, 'Preto')
    else: tupla = (tamanho, 'Azul')
  roupas.append(tupla)
  print(roupas)

contP = 0
contM = 0
contG = 0
cores = []

for item in roupas:
  if item[0] == 'P' or item[0] == 'p':
    contP = contP + 1
  else:
    if item[0] == 'M' or item[0] == 'm':
      contM = contM + 1
    else:
      contG = contG + 1
  cores.append(item[1])

totalTamanho = []
totalTamanho.append((f'Pequeno {contP}'))
totalTamanho.append((f'Médio {contM}'))
totalTamanho.append((f'Grande{contG}'))
print(totalTamanho)

maior = 0
tamanho = ''

for item in totalTamanho:
  if item[1] > maior:
    maior = item[1]
    tamanho = item[0]
print(f'Tamanho mais vendido: {tamanho} vendou {roupas}')
print(f'Quantidade de tamanho M vendidas: {totalTamanho[1]}')
print('Quantidade de peças Brancas vendidas: ', cores.count('Branco'))
print('Quantidade de peças Pretas vendidas: ', cores.count('Preto'))
print('Quantidade de peças Azuis vendidas: ', cores.count('Azul'))


#  – Faça um programa que leia frases e as armazena
# em uma lista. A seguir, segmente cada frase em palavras,
# armazenando os tokens em uma lista de lista.

frases = ['Hoje foi um dia interessante.', 'Preciso organizar melhor os meus treinos diários.', 'Caguei a minha alimentação essa semana.']

for sentenca in frases:
  print(sentenca)

#Tokenização: Seguimentação em palavras | Lista de listas

tokens = []

for sentenca in frases:
  tokens.append(sentenca.split())

for sentenca in tokens:
  print(f'Palavras da sentença: {sentenca}')
  for palavra in sentenca:
    print(palavra)

