import matplotlib.pyplot as plt

listax = []
listay = []

for x in range (10):
  listax.append(x)
  listay.append(x**2)
  plt.plot(listax,listay)
  plt.show()

import matplotlib.pyplot as plt

listax = [x for x in range (10)]
listay = [x**2 for x in range (10)]

plt.plot(listax,listay, 'ro')
plt.show()

import matplotlib.pyplot as plt

listax = [x for x in range (10)]
listay = [x**2 for x in range (10)]
listay2 = [x**3 for x in range (10)]

plt.plot(listax,listay, 'r-')
plt.plot(listax,listay2, 'bo')
plt.show()

import matplotlib.pyplot as plt

listax = [x for x in range (10)]
listay = [x**2 for x in range (10)]
listay2 = [x**3 for x in range (10)]

plt.plot(listax,listay, 'r-', label = "$x^2$")
plt.plot(listax,listay2, 'bo', label = "$x^3$")

plt.title("$x^2$ e $x^3$")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import random

random.seed(42)
anos = [a for a in range (1990,2010)]
valores = [random.randint(100,1500) for v in range (len(anos))]

plt.bar(anos,valores)
plt.xticks(range(1990, 2010, 2))
plt.show()

import matplotlib.pyplot as plt
import random

random.seed(42)

valores = [random.randint(0,11) for v in range (0,100)]
x = [v + 0.5 for v in range (0,11)]
plt.hist(valores,x)
plt.show()

def carregarDados (nomeArq):
  aux = []
  with open(nomeArq) as csv:
    csv.readline()
    for linha in csv:
      nova = [float(val) for val in linha.split(',')]
      aux.append(nova)
  return aux

dados = carregarDados ('sample_data/california_housing_test.csv')

longitudes = [aux[0] for aux in dados]
latitudes = [aux[1] for aux in dados]

#plt.plot(longitudes, latitudes, 'bo')
plt.scatter(longitudes, latitudes, s=1)
plt.show()

import folium

map = folium.Map(location = [36.7783, -119.4179],
                 zoom_start = 6, min_zoom = 5)

for aux in dados:
  folium.CircleMarker(radius = 1, location = [aux[1], aux[0]]).add_to (map)

map

import folium
from folium.plugins import MarkerCluster

# Definindo a variável dados com três locais de exemplo
dados = [
    [36.7783, -119.4179],  # Local 1
    [34.0522, -118.2437],  # Local 2
    [37.7749, -122.4194]   # Local 3
]

# Criando o mapa
map = folium.Map(location=[36.7783, -119.4179], zoom_start=6, min_zoom=5)
marker_cluster = MarkerCluster().add_to(map)

# Adicionando marcadores ao mapa
for aux in dados:
    folium.CircleMarker(radius=1, location=[aux[0], aux[1]]).add_to(marker_cluster)

# Exibindo o mapa
map

import folium
from folium.plugins import HeatMap

# Supondo que dados já esteja definido corretamente
# dados = [...]

map = folium.Map(location=[36.7783, -119.4179], zoom_start=6, min_zoom=5)

# Preparando os dados para o HeatMap
aux2 = [[aux[1], aux[0], aux[7]] for aux in dados]  # aux[7]: median income

# Adicionando o HeatMap ao mapa
HeatMap(aux2, min_opacity=0.1).add_to(map)

# Salvando o mapa em um arquivo HTML
map.save("meu_mapa.html")

import math
import matplotlib.pyplot as plt  # Importando a biblioteca para plotar

g = 9.81  # Aceleração da gravidade em m/s^2
ang = float(input("Ângulo (em graus): "))  # Lê o ângulo em graus
v0 = float(input("Vel. inicial (m/s): "))  # Velocidade inicial
y0 = float(input("Altura inicial (metros): "))  # Altura inicial
listax = []  # Lista para armazenar os valores de x
listay = []  # Lista para armazenar os valores de y

# Converte ângulo para radianos
ang = math.radians(ang)

y = y0  # Inicializa y com a altura inicial
x = 0  # Inicializa x
delta_x = 0.1  # Incremento em x para cada passo do loop

while y >= 0:  # Enquanto a altura for maior ou igual a zero
    listax.append(x)
    listay.append(y)
    # Atualiza o valor de x
    x += delta_x
    # Calcula o novo valor de y
    y = x * math.tan(ang) - (g * x**2) / (2 * v0**2 * math.cos(ang)**2) + y0

# Configuração dos rótulos dos eixos
plt.xlabel("Distância (m)")
plt.ylabel("Altura (m)")

# Plotagem dos pontos e exibição do gráfico
plt.plot(listax, listay, 'bo-')  # 'bo-' cria um gráfico de linha com marcadores em forma de bola azul
plt.grid(True)  # Adiciona grade ao gráfico para melhor visualização
plt.show()  # Exibe o gráfico


#  Aplicação dos Números de Fibonacci
# • 1, 1, 2, 3, 5, 8, 13, 21, 34,...
# • Possuem propriedades interessantes
# • A divisão de um número pelo anterior (a partir do terceiro) gera sempre o mesmo resultado: uma aproximação de um número conhecido como razão áurea
# • Razão Áurea
# • 1,6180339887...
# • Esse número pode ser encontrado em diversos locais, especialmente na Natureza
# • Esta figura de um girassol mostra a distribuição das sementes
# • Há uma relação direta do posicionamento delas com a razão áurea!

# Relação em relação ao ângulo através do qual as sementes são “posicionadas” na flor
# • Algoritmo para gerar as coordenadas:
# 1. Calcular o “ângulo áureo”:
# 2. Inicializar ângulo atual com zero
# 3. Criar duas listas vazias para as coordenadas
# 4. Repetir usando um contador (quantidade de sementes):
# • Calcular a distância através da raiz quadrada do contador
# • Adicionar o ângulo áureo ao atual
# • Calcular posição da semente:
# • Acrescentar as coordenadas nas listas de pontos

!pip install cmcrameri

import matplotlib.pyplot as plt
import cmcrameri.cm as cmc
import math

listax = []
listay = []
dists = [] # distâncias ao centro
phi = (1 + math.sqrt(5))/2
angAureo = 360 - 360/phi

ang = 0
for cont in range(3000):
  dist = math.sqrt(cont)
  ang = ang + angAureo
  ang_rad = math.radians(ang)
  x = dist * math.cos(ang_rad)
  y = dist * math.sin(ang_rad)
  listax.append(x)
  listay.append(y)
  dists.append(dist)

plt.figure(figsize=(10,10))

# https://matplotlib.org/stable/tutorials/colors/colormaps.html
plt.scatter(listax,listay,c=dists,cmap=cmc.bamako)

def fibo (n):
  n1 = 1
  n2 = 1
  print(f'{n1:3}')
  for cont in range (n):
    print(f'{n2:3}: ', end='')
    n1, n2 = n2, n1 + n2
    print(f'{n1/n2}')
  print()
fibo(15)

dic = {}
dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"
nome = ''
while nome != "fim":
  nome = input("Nome a procurar (fim para encerrar): ")
  if nome != "fim":
    if nome in dic:
      print(f"Telefone: {dic[nome]}")
    else:
      print("Nome não encontrado!")

nome = ""
while nome != "fim":
  print(f"Tamanho do dicionário: {len(dic)}")
  print(dic)
  nome = input("Nome a remover (fim para encerrar): ")
  if nome != "fim":
    if nome in dic:
      del dic[nome]
      print("Nome removido!")
    else:
      print("Nome não encontrado!")


dic = {}
dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"

print(dic.keys())
print(dic.values())
print(dic.items())

print(f"Telefone de Fulano: {dic.get('Fulano')}")
print(f"Telefone de Veltrano: {dic.get('Veltrano')}")

dic = {}

dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"
dic["Pedro"] = "99123-2432"

for k in dic.keys():
  print(f"Chave: {k}")
for v in dic.values():
  print(f"Valor: {v}")
  print("Chaves e valores em ordem de inclusão:")
for k,v in dic.items():
  print(f"{k:8} -> {v}")
  print("Ordenado pelas chaves:")
for k,v in sorted(dic.items()):
  print(f"{k:8} -> {v}")
  print("Ordenado pelos valores:")
for k,v in sorted(dic.items(),
  key=lambda x: x[1]):
    print(f"{k:8} -> {v}")