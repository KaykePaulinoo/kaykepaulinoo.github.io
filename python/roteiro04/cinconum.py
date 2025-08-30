contador_pares = 0
while contador_pares <5:
    numero_usuario = int(input('digite um numero'))
    numero_par = int(numero_usuario)

    if numero_par %2 ==0:
        print(f'numero par encontrado: {numero_par}')
        contador_pares += 1
        
   
