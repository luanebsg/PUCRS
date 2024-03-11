#Jogo da Forca

# Implementar o popular Jogo da Forca, onde
# o objetivo é descobrir a palavra escolhida
# pelo computador:
# • No início, o computador escolhe uma palavra
# • A cada jogada, o usuário “chuta” uma letra
# • Se a letra não existir na palavra, ele perde a
# jogada
# • Se a letra existir, ela é exibida na posição correta
# na palavra
# • Se completar o desenho do homem na forca, o
# jogo é encerrado

import random

def sorteio():
  return random.choice([
    "cão", "gato", "peixe", "pássaro", "hamster", 
    "coelho", "tartaruga", "cobra", "sapo", "lagarto", 
    "cavalo", "vaca", "porco", "ovelha", "cabra", 
    "galinha", "pato", "ganso", "peru", "abelha"
])

def forca(vidas):
  if vidas == 0:
    print("""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """)
  elif vidas == 1:
    print("""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """)
  elif vidas == 2:
    print("""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """)
  elif vidas == 3:
    print("""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """)
  elif vidas == 4:
    print("""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """)
  elif vidas == 5:
    print("""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """)
  else:
    print("""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """)
  
import random

# ... (As funções sorteio() e forca() não mudam)

# 1. Sorteio da palavra
palavra = sorteio()
print(palavra)  # Você pode querer remover isso mais tarde para não mostrar a palavra no início.

# 2. Palavra com '_'
tam = len(palavra)
adivinhada = ["_"] * tam
vidas = 6
letras = []

# 3. Iniciar o jogo
jogoAtivo = True
while jogoAtivo:
  # Exibir estado do jogo
  print()
  forca(vidas)
  print()
  print(" ".join(adivinhada))
  print()
  print(f'Letras já escolhidas: {" ".join(letras)}')

  # 4. Digitação de letra válida
  while True:
    letra = input('Escolha uma letra: ').lower()
    if letra not in letras and len(letra) == 1 and letra.isalpha():
      letras.append(letra)
      break
    else:
      print('Letra inválida ou já foi escolhida, tente novamente.')

  # 5. Verificar se a letra está na palavra
  if letra in palavra:
    # Atualizar 'adivinhada' com a letra correta nas posições correspondentes
    for pos, char in enumerate(palavra):
      if char == letra:
        adivinhada[pos] = letra
  else:
    print('Esta letra não está na palavra.')
    vidas -= 1

  # 6. Verificar condição de vitória ou derrota
  if "_" not in adivinhada:
    print("Parabéns! Você adivinhou a palavra!")
    jogoAtivo = False
  elif vidas == 0:
    print("Que pena! Suas vidas acabaram.")
    jogoAtivo = False