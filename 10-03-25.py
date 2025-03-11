number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

soma = number1 + number2
print(soma)

metros = float(input("Digite a quantidade de metros: "))

milimetros = metros * 1000
print('o valor em milimetros %.2f' % milimetros)

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
print(total_segundos)

salario = float(input("Digite o salário: "))
aumento = float(input("Digite o aumento: "))
salario_final = salario + (salario * aumento / 100)
print(salario_final)

mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_do_desconto = mercadoria * desconto / 100
valor_final = mercadoria - valor_do_desconto
print(f'O valor final é de R${valor_final:.2f} e o desconto foi de R${valor_do_desconto:.2f}')

km = float(input("Digite a quantidade de km: "))
velocidade = float(input("Digite a velocidade média: "))
tempo = km / velocidade

print(f'O tempo estimado é de {tempo:.2f} horas')

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = ((9 * celsius) / 5) + 32
print(f'A temperatura em Fahrenheit é de {fahrenheit:.2f}')

km = float(input("Digite a quantidade de km: "))
dias = int(input("Digite a quantidade de dias alugado: "))
valor = (dias * 60) + (km * 0.15)
print(f'O valor a ser pago é de R${valor:.2f}')

cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite a quantidade de anos fumando: "))
death = ((10 * cigarros) * (anos * 365)) / 1440
print(f'Você perdeu {death:.2f} dias de vida')
