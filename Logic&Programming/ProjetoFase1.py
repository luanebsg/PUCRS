# Validação mês e temperatura
# Dá ao usuário 3 tentativas para inserir um mês válido

month_str = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
degree_box = {}
months_entered = set()

while len(months_entered) < 12:

  for year_2021 in month_str:

    for i in range(4):
      month = int(input('Selecione o mês do ano em forma numérica (1 a 12): '))
      if month >= 1 and month <= 12 and month not in months_entered:
        print(f"Mês selecionado: {month_str[month - 1]}")
        months_entered.add(month)
        break
      else:
        print('Mês inválido, tente novamente.')
        if i == 3:  # Última tentativa
          print('Você excedeu o número de tentativas inválidas.')
          exit()

    for i in range(4):
      degrees_str = input(f'Informe a Temperatura em Celsius do mês de {month_str[month - 1]}: ')
      degrees_str = degrees_str.replace(',', '.')
      degrees = float(degrees_str)
      if degrees >= -60 and degrees <= 50:
        print(f"Mês: {month_str[month - 1]}, Temperatura: {degrees} ºC")
        degree_box[month_str[month - 1]] = degrees
        break
        9
      else:
        print('Temperatura inválida, tente novamente.')
        if i == 3:  # Última tentativa
          print('Você excedeu o número de tentativas inválidas.')
          exit()
print('Todos os meses e temperaturas foram inseridos com sucesso.')