def calcular_fatorial(numero):
    if numero < 0:
        return "ERRO: O numero nao pode ser negativo"
    elif numero == 0:
     return 1
    else: 
       resultado = 1 
       for i in range(1, numero + 1):
          resultado *= i
    return resultado
numeroteste = 4
print(f"O fatorial do {numeroteste} é: {calcular_fatorial(numeroteste)}")
numerotestenegativo = -8
print(f"tentando calcular o fatorial de {numerotestenegativo} {calcular_fatorial(numerotestenegativo)}")