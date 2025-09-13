N = int(input("Digite um numero inteiro: "))
if N <= 0:
    print("Porfavor digite um numero valido")
else:
     soma_pares = 0
     for numero in range (2 , N + 1):
          if numero %2 == 0:
               soma_pares += numero
               print(f"A soma dos numeros inteiros de 1 ate {N} é: {soma_pares}")
