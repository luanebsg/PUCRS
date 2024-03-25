# Aluna: Luane Barcellos
# Lógica e Programação de Computadores

import datetime
import matplotlib.pyplot as plt
import calendar # Para caso o usuário decida ver os dados de um único mês.

caminho_arquivo = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"

#Carga e Preparação de Dados
def carregar_dados(caminho_arquivo):
  dados = []
  with open(caminho_arquivo, 'r') as arquivo:
    next(arquivo)  # Ignora o cabeçalho
    for linha in arquivo:
      partes       = linha.strip().split(',')
      data         = datetime.datetime.strptime(partes[0], "%d/%m/%Y")
      precipitacao = float(partes[1]) if partes[1] else None
      temp_max     = float(partes[2]) if partes[2] else None
      temp_min     = float(partes[3]) if partes[3] else None
      umidade      = float(partes[4]) if partes[4] else None
      vento        = float(partes[5]) if partes[5] else None
      dados.append((data, precipitacao, temp_max, temp_min, umidade, vento))
    return dados

#---------------------------------------------------------------------------------------------------------------------------------------#

## Definição das funções ##

# a) Visualização de Intervalo de Dados em Modo Texto

# Função para visualizar dados de um intervalo específico
def visualizar_intervalo(dados, data_inicio, data_fim, categoria):
  print('-----------------------------------------------------------------------------------------------------------------')
  print('a) Visualização de Intervalo de Dados em Modo Texto')
  print("Data, Categoria Selecionada")
  for registro in dados:
    if data_inicio <= registro[0] <= data_fim:
      if categoria == 1:  # Todos os dados
        print(f"{registro[0].strftime('%d/%m/%Y')}, Precipitação: {registro[1]}, Temp. Máx: {registro[2]}, Temp. Min: {registro[3]}, Umidade: {registro[4]}, Velocidade do Vento: {registro[5]}")
      elif categoria == 2:  # Precipitação
        print(f"{registro[0].strftime('%d/%m/%Y')}, Precipitação: {registro[1]}")
      elif categoria == 3:  # Temperatura
        print(f"{registro[0].strftime('%d/%m/%Y')}, Temp. Máx: {registro[2]}, Temp. Min: {registro[3]}")
      elif categoria == 4:  # Umidade e vento
        print(f"{registro[0].strftime('%d/%m/%Y')}, Umidade: {registro[4]}, Velocidade do Vento: {registro[5]}")


# b) Mês Mais Chuvoso

# Função para encontrar o mês mais chuvoso
def mes_mais_chuvoso(dados):
    print('----------------------------------------------------------------------------------------------------------------')
    print('b) Mês Mais Chuvoso do Documento')
    precipitacao_por_mes = {}
    for registro in dados:
      mes_ano = registro[0].strftime("%m/%Y")
      precipitacao = registro[1] if registro[1] is not None else 0
      if mes_ano in precipitacao_por_mes:
        precipitacao_por_mes[mes_ano] += precipitacao
      else:
        precipitacao_por_mes[mes_ano] = precipitacao

    mes_mais_chuvoso = max(precipitacao_por_mes, key=precipitacao_por_mes.get)
    print(f"Mês mais chuvoso: {mes_mais_chuvoso} com {precipitacao_por_mes[mes_mais_chuvoso]} mm")
    print('----------------------------------------------------------------------------------------------------------------')


# c) Média da Temperatura Mínima para um Mês Específico nos Últimos 11 Anos
def calcular_media_temp_minima_mensal(dados, mes, inicio, fim):
  print('--------------------------------------------------------------------------------------------------------------')
  print('c) Média da temperatura mínima de um determinado mês nos últimos 11 anos (2006 a 2016)')

  # Define a data final considerando apenas até 10/07/2016
  data_final = datetime.datetime(2016, 7, 10)

  # Verifica se o mês de análise é posterior a julho de 2016
  if mes > 7:
    print("O mês selecionado é posterior aos dados disponíveis (após 10/07/2016).")

  # Verifica se a data final fornecida pelo usuário está após 10/07/2016
  if fim > data_final.year:
    print("A data final fornecida é posterior aos dados disponíveis (após 10/07/2016).")
    fim = data_final.year

  # Dicionário para armazenar as médias de temperatura mínima
  medias_mensais = {}
  for ano in range(inicio, fim + 1):
    temperaturas_mes = []
    for registro in dados:
      if registro[0].year == ano and registro[0].month == mes:
        if registro[0] <= data_final:
          if registro[3] is not None:
            temperaturas_mes.append(registro[3])

        # Calcula a média das temperaturas mínimas do mês no ano atual
    if temperaturas_mes:
      media = sum(temperaturas_mes) / len(temperaturas_mes)
      medias_mensais[f"{datetime.date(1900, mes, 1).strftime('%B')}{ano}"] = media
      print(f"{datetime.date(1900, mes, 1).strftime('%m')}/{ano}: Média da temperatura mínima = {media:.2f}°C")
  return medias_mensais

#Validação do mês de análise
def validar_mes(mes):
  while True:
    try:
      mes = int(mes)
      if 1 <= mes <= 12:
        return mes
      else:
        print("Por favor, insira um número de mês válido (1-12).")
        mes = input("Digite o número do mês para análise (1-12): ")
    except ValueError:
      print("Por favor, insira um número inteiro para o mês.")
      mes = input("Digite o número do mês para análise (1-12): ")

# d) Gráfico de Barras com Médias de Temperatura Mínima

def gerar_grafico_barras(medias_anuais):
  print('-----------------------------------------------------------------------------------------------------------------')
  print('d) Gráfico de Barras com Médias de Temperatura Mínima')
  anos = list(medias_anuais.keys())
  medias = list(medias_anuais.values())

  plt.figure(figsize=(10, 6))
  plt.bar(anos, medias, color='skyblue')
  plt.xlabel('Ano')
  plt.ylabel('Temperatura Mínima Média (°C)')
  plt.title('Média da Temperatura Mínima Mensal por Ano')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()


# Função para solicitar uma data válida ao usuário

def solicitar_data(mensagem):
  while True:
    data_str = input(mensagem)
    try:
      data = datetime.datetime.strptime(data_str, "%d/%m/%Y")
      if 1900 <= data.year <= 2100 and 1 <= data.month <= 12 and 1 <= data.day <= 31:
        if not (data.day > 28 and data.month == 2):  # Verifica se fevereiro tem mais de 28 dias
          return data
        else:
          print("Fevereiro não pode ter mais de 28 dias (ou 29 em ano bissexto).")
      else:
        print("Data fora do intervalo permitido. Por favor, insira uma data válida.")
    except ValueError:
      print("Formato de data inválido. Por favor, use dd/mm/yyyy.")


# Função para solicitar uma categoria válida ao usuário
def solicitar_categoria():
  while True:
    try:
      categoria = int(input("Selecione a categoria: 1) Todos os dados, 2) Precipitação, 3) Temperatura, 4) Umidade e vento: "))
      if 1 <= categoria <= 4:
        return categoria
      else:
        print("Por favor, selecione um número entre 1 e 4.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número inteiro.")

# Função para coletar as entradas do usuário
def coletar_entrada_usuario():
  print("Por favor, forneça as informações solicitadas abaixo.")
  while True:
    try:
      # Coleta do mês e ano para a data de início
      while True:
        try:
          mes_inicio = int(input("Digite o mês de início (1-12): "))
          ano_inicio = int(input("Digite o ano de início (yyyy): "))
          if 1 <= mes_inicio <= 12:
            break
          else:
            print("O mês deve estar entre 1 e 12. Por favor, tente novamente.")
        except ValueError:
          print("Entrada inválida. Por favor, insira um número inteiro para o mês.")
            # Coleta do mês e ano para a data de fim
      while True:
        try:
          mes_fim = int(input("Digite o mês de fim (1-12): "))
          ano_fim = int(input("Digite o ano de fim (yyyy): "))
          if 1 <= mes_fim <= 12:
            break
          else:
            print("O mês deve estar entre 1 e 12. Por favor, tente novamente.")
        except ValueError:
          print("Entrada inválida. Por favor, insira um número inteiro para o mês.")


      # Cria as datas de início e fim
      data_inicio = datetime.datetime(year=ano_inicio, month=mes_inicio, day=1)

      #Função calendar.monthrange para caso o usuário deseje ver o dados de um único mês do mesmo ano
      data_fim = datetime.datetime(year=ano_fim, month=mes_fim, day = calendar.monthrange(ano_fim,mes_fim)[1])
      if data_fim < data_inicio:
        print('Data final é maior do que data incial. Por favor, insira uma data válida para coleta de dados.')
        continue

      # Seleção da categoria
      while True:
        try:
          categoria = int(input("Selecione a categoria desejada:\n"
                                          "1) Todos os dados\n"
                                          "2) Apenas precipitação\n"
                                          "3) Apenas temperatura\n"
                                          "4) Apenas umidade e vento\n"
                                          "Digite o número correspondente à categoria: "))
          if 1 <= categoria <= 4:
            return data_inicio, data_fim, categoria
          else:
            print("Por favor, selecione uma opção válida.")
        except ValueError:
          print("Entrada inválida. Por favor, insira um número inteiro.")
    except ValueError:
      print("Entrada inválida. Por favor, insira um número inteiro para o ano.")



# Função para verificar se o mês e ano existem nos dados
def verificar_existencia_mes_ano(dados, mes, ano):
  for registro in dados:
    if registro[0].month == mes and registro[0].year == ano:
      return True
  return False

# e) Média Geral da Temperatura Mínima

def calcular_media_geral(medias_anuais):
  print('----------------------------------------------------------------------------------------------------------------')
  print('e)')
  if medias_anuais:
    media_geral = sum(medias_anuais.values()) / len(medias_anuais)
    print(f"Média Geral da Temperatura Mínima: {media_geral:.2f}°C")
    return media_geral
  else:
    print("Não há dados disponíveis para calcular a média geral.")
    return None


#--------------------------------------------------------------------------------------------------------------------#

# Dados
dados_climaticos = carregar_dados(caminho_arquivo)

# Coleta do usuário
data_inicio, data_fim, categoria = coletar_entrada_usuario()

# Chamada de funções utilizando as entradas coletadas
visualizar_intervalo(dados_climaticos, data_inicio, data_fim, categoria)

#---------------------------------------------------------------------------------------------------------------------#

# Análise e Visualização de Dados

# Mês mais chuvoso
mes_mais_chuvoso(dados_climaticos)

# Média mínima para um mês específico nos últimos 11 anos
mes_escolhido = input("Digite o número do mês para análise (1-12): ")
mes_escolhido = validar_mes(mes_escolhido)
print("Mês escolhido:", mes_escolhido)
medias_anuais = calcular_media_temp_minima_mensal(dados_climaticos, mes_escolhido, 2006, 2016)

# Gráfico de barras
gerar_grafico_barras(medias_anuais)

# Média geral da temperatura mínima de um mês nos últimos 11 anos
media_geral = calcular_media_geral(medias_anuais)

#-----------------------------------------------------------------------------------------------------------------------------#

# Salvando Resultados em Arquivo

def salvar_resultados_media_temp_minima(caminho_arquivo_saida, medias_anuais, media_geral):
  with open(caminho_arquivo_saida, 'w') as arquivo:
    arquivo.write("Ano, Média Temperatura Mínima (°C)\n")
    for ano, media in medias_anuais.items():
      arquivo.write(f"{ano}, {media:.2f}\n")
    arquivo.write(f"\nMédia Geral da Temperatura Mínima (2006-2016): {media_geral:.2f}°C\n")

# chamada da função para salvar resultados
salvar_resultados_media_temp_minima("resultados_temperatura_minima.txt", medias_anuais, media_geral)
