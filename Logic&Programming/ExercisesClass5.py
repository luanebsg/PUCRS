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

# • Revisiting example 4 (Heron’s algorithm):
# 1. Start with a “kick”, n
# 2. Repeat a certain number of times:
# 1. The next “guess” will be the average between n and 𝑥/𝑛
# 3. Show off the final “kick”
# • How many times should we run?
# • Run with different values ​​to test – what do you observe?
# We can end the loop when the difference between the last value calculated and the current value is very small
# • How to change the algorithm?
# We can end the loop when the difference between the last value calculated and the current value is very small
# • How to change the algorithm?
# • Mathematical function: abs (value absolute)

num = int(input("Valor Desejado: "))
total = int(input("Quantidade de repetições: "))

approx = 1
previous = 0
for cont in range (1, total + 1):
  approx = (approx + num / approx) / 2
  print(f'{cont:3} {approx:.5f}')
  dif = abs (approx - previous)
  if dif < 0.001:
    break
  previous = approx

print(f'Approximate root: {approx:.5f}')

# Repetition is often used for problems involving statistics about a set of data
# • Example: read 10 float values, representing heights of people, calculate and display average heights
# Remembering: the concept of accumulator
# • We need a variable to accumulate the sum of the heights, in order to calculate the average at the end
# 𝑚𝑒𝑑𝑖𝑎 = 𝑠𝑜𝑚𝑎 / 10 = 1.77
# Remembering: the concept of accumulator
# • We need a variable to accumulate the sum of the heights, in order to calculate the average at the end

soma = 0
for cont in range(10):
  alt = float(input('Digite uma altura: '))
  soma = soma + alt

media = soma/10
print(f'Media: {media:.3f}')

# Improve the previous program by discovering and displaying the greatest height entered
# • The solution also involves the use of another accumulator, but now to store the greatest height found so far
# To avoid spending time typing values, we will use the random module already worked on in class 4

import random
sum = 0
maior = 0
for cont in range (10):
  alt = random.uniform(1.5, 2.10)
  sum = sum + alt
  if alt > maior:
    maior = alt
media = soma/10
print(f"Media: {media:.3f}")
print(f"Maior altura: {maior}")

# 50 Engineering students were interviewed:

# • The following data were collected from each student: age, semester and course
# • The program must “read” (sort) the students’ data, calculate and write:
# • average age of students
# • older student course
# • number of students in the 5th semester
# • Understanding the problem requirements
# • Inputs: sequence of ages, courses, semesters

# Understanding the problem requirements:
# • Outputs:
# • average age of students: sum of ages
# • oldest student's course: course, oldest age found
# • number of students in the 5th semester: accumulator for totalization

import random

sumAge = 0
courseOldest = ""
ageOldest = 0
students5oSem = 0

for cont in range(50):
  #Sortition
  age = random.randint(18, 60)
  course = random.choice(["Eng. Civil", "Eng.Mec", "Eng. Química", "Eng. Prod."])
  semester = random.randint(1,10)
  # Statistics collection
  # Average ages: it is necessary to add the ages
  sumAge += age
  # Older Student Course
  if age > ageOldest:
    ageOldest = age
    courseOldest = course
  # Total number of students in 5th. semester
  if semester == 5:
    students5oSem += 1

averageAge = sumAge // 50
print(f"Average age: {averageAge}")
print(f"Oldest student's course ({ageOldest} years): {courseOldest}")
print(f"Total number of students in the 5th year: {students5oSem}")

#Strings

text = "Esta é uma String"

print(text[0])
print(text[5])
print(text[-1])
print(text[-6])

# • Concatenation and repetition operators

texto = "Esta"
print(texto + " é uma string")
print(texto * 3)
print('=' * 30)
# Combinando os dois operadores
result = texto * 4 + " é uma " + "String" * 3
print(result)

#Slicing

texto = "Esta é uma String"

print(texto[0:4])
print(texto[7:10])
print(texto[-6:])
print(texto[:6])

texto = "Esta é uma String"

print(texto[0:10:2])
print(texto[::2])
print(texto[::-1])

texto = "Esta é uma String"

texto = texto[:3] + "e" + texto[4:]
print(texto)

# Comparação de strings
# "outro texto" vem antes de "texto"

texto1 = "texto"
texto2 = "outro texto"
if texto1 < texto2:
  print(f'"{texto1}" vem antes de "{texto2}"')
elif texto2 < texto1:
  print(f'"{texto2}" vem antes de "{texto1}"')
else:
  print(f'"{texto1}" é igual a "{texto2}"')

# Belonging Operator
# • Any string allows you to easily check whether a sequence of
# characters are inside it
# • Membership operator: in

# • Belonging operator
# Result depends on the content of the strings


text1 = input("Enter a sentence: ")
text2 = input("Enter a word: ")
if text2 in text1:
  print(f"{text2} is in the sentence")
else:
  print(f"{text2} is not in the sentence...")

# Getting the length of a string (len function)

texto = input("Digite uma frase: ")
print(f"O comprimento da frase é {len(texto)} caracteres")

# • Passing directly through all characters in a string

texto = input("Digite uma frase: ")
for caractere in texto:
  print(caractere)

# Passing through all characters in a string, using access by index

texto = input("Digite uma frase: ")
for pos in range(len(texto)):
  print(texto[pos])

# Program to check if a typed string matches the contrary (palindrome)
# • Example:

# revive _ revive

# • How to solve?

# • Remembering that it is possible easily reverse a string (slicing)

texto = input("Digite uma frase: ")

print(f'Iinvertida: {texto[::-1]}')
if texto != texto[::-1]:
  print("A frase não é um palíndromo...")
else:
  print("A frase é um palíndromo!")

# * Program to count the number of vowels present in a string

texto = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
totalVogais = 0

for letra in texto:
  if letra in vogais:
    totalVogais += 1
    
print(f"Quantidade de vogais: {totalVogais}")

# Programa para verificar se uma senha digitada é “forte”
# • Mínimo de 8 caracteres
# • Pelo menos uma letra maiúscula
# • Pelo menos um dígito entre 0-9
# • Pelo menos um caractere de pontuação

# Programa para verificar se uma senha digitada é “forte”
# • Mínimo de 8 caracteres
# • Pelo menos uma letra maiúscula
# • Pelo menos um dígito entre 0-9
# • Pelo menos um caractere de pontuação
# • O pacote string tem algumas constantes que podem ajudar:
# • string.uppercase: letras maiúsculas
# • string.digits: dígitos de 0 a 9
# • string.punctuation: caracteres de pontuação

import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

senha = input("Senha: ")
maiuscula = False
digito = False
pontuacao = False

if len(senha) < 8:
  print("Erro: senha muito curta")
else:
  for letra in senha:
    if letra in string.ascii_uppercase:
      maiuscula = True
    if letra in string.digits:
      digito = True
    if letra in string.punctuation:
      pontuacao = True

if maiuscula == False or digito == False or pontuacao == False:
  if maiuscula == False:
    print("Erro: senha não tem maiúsculas")
  if digito == False:
    print("Erro: senha não tem dígitos")
  if pontuacao == False:
    print("Erro: senha não tem caractere de pontuação")
else:
  print("Senha válida!")

# • Programa para mostrar as iniciais de um nome com o(s)
# sobrenomes, digitados em uma única string

nome = input("Digite um nome completo: ")
inicio = True

for letra in nome:
  if inicio:
    print(f"{letra}. ", end="")
    inicio = False
  elif letra == " ":
    inicio = True
  
# Implementar o Jogo da Adivinhação, onde o objetivo é adivinhar um número sorteado pelo computador:
# • No início, o computador sorteia um número entre 1 e 100
# • O jogador tem 10 chances para adivinhar o número
# • A cada chance, o computador deve informar se o número é maior, menor ou se é igual ao sorteado
# • Se for igual, o jogo termina e o jogador é informado da vitória
# • Quando acabarem as chances, o jogo também termina e o jogador é informado da derrota

import random

sorteado = random.randint(1,100)
#print(f'Sorteado: {sorteado}')
acertou = False

for tent in range (1,11):
  print(f'Tentativa: {tent}: ', end = "")
  num = int(input())
  if num < sorteado:
    print('Tente um número maior...')
  elif num > sorteado:
    print('Tente um número menor...')
  else:
    acertou = True
    break

if acertou:
    print('Parabéns! Você acertou.')
else:
  print(f'Que pena, você perdeu... O número era {sorteado}')

# Foram entrevistados 2000 habitantes de uma cidade. De cada habitante foram coletados os seguintes dados: idade, renda, gênero e número de filhos. O programa deve obter os dados desses habitantes, calcular e escrever:
# a) media de renda
# b) media de idade de quem tem mais de 3 filhos
# c) quantidade de homens com menos de 30 anos
# d) media do número de filhos
# e) renda do homem mais velho
# f) idade da mulher com maior renda

import random

somaRendas = 0
somaIdades = 0
HomensMenor30 = 0
somaFilhos = 0
mais3Filhos = 0
rendaHomemMaisVelho = 0
idadeHomemMaisVelho = 0
idadeMulherMaiorRenda = 0
mulherMaiorRenda = 0

totalHabitantes = 2000

#Sorteio
for cont in range(2000):
  idade = random.randint(18,80)
  renda = random.randint(1200,12000)
  genero = random.choice(['M', 'H'])
  filhos = random.randint(0,5)

  #1. Média de Renda
  somaRendas += renda

  #2. Média de idade com mais de três filhos
  if filhos > 3:
    somaIdades += idade
    mais3Filhos += 1

  #3. Homens com menos de 30 anos
  if genero == 'H' and idade < 30:
    HomensMenor30 += 1

  #4. Média de filhos
  somaFilhos += filhos

  #5. Renda homem mais velho
  if genero == 'H' and idade > idadeHomemMaisVelho:
    idadeHomemMaisVelho = idade
    rendaHomemMaisVelho = renda

  #6. Idade da mulher com maior renda
  if genero == 'M' and renda > mulherMaiorRenda:
    idadeMulherMaiorRenda = idade
    mulherMaiorRenda = renda

#Mostrar os Resultados

mediaRenda = somaRendas / totalHabitantes
media3Filhos = somaIdades // mais3Filhos
mediaFilhos = somaFilhos // totalHabitantes

print(f'Média de renda da população: {mediaRenda}')
print(f'Média com mais de 3 filhos: {media3Filhos}')
print(f'Homens com menos de 30 anos: {HomensMenor30}')
print(f'Média número de filhos: {mediaFilhos}')
print(f'Renda do Homem mais Velho: {rendaHomemMaisVelho}')
print(f'Idade da Mulher com maior renda: {idadeMulherMaiorRenda}')
