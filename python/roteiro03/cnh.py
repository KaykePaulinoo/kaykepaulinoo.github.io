from datetime import datetime as dt

ano_hj = dt.now().year
mes_hj = dt.now().month
dia_hj = dt.now().day

ano = int(input("digite o ano do seu nascimento: "))
mes = int(input("digite o mês do seu nascimento: "))
dia = int(input("digite o dia do seu nascimento: "))

idade =  ano_hj - ano

if (mes_hj, dia_hj) < ( mes, dia):
 idade = idade - 1

print(f'Você tem {idade} anos')
if idade >= 18:
   print ('Voce ja pode tirar CNH')
else:
   print('Você não pode tirar CNH')